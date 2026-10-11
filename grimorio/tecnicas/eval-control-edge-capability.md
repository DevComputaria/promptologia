---
id: eval-control-edge-capability
titulo: Eval de feitiço — control, edge, capability
camara: tecnicas
categoria: harness
objetivo: Gerar casos conferíveis que provam se um prompt aguenta, quebra ou finge que aguenta.
entrada: [feitico sob teste, saida de referencia opcional]
saida: markdown
placeholders: ["{{FEITICO}}", "{{RESTRICAO_DE_DOMINIO}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: nenhum
proveniencia: original
fonte: ""
substitui: ""
---

# Eval de feitiço — control, edge, capability

## Objetivo

Dado um prompt do grimório (ou de fora), produzir a bateria mínima que separa três situações: o feitiço faz o óbvio, o feitiço se perde na entrada suja, o feitiço cumpre a promessa difícil que ele mesmo escreveu. A saída desta técnica é a bateria, não a resposta da tarefa original.

Um caso só entra na bateria se um humano, ou um script, decide acerto ou erro em menos de um minuto sem discutir gosto.

## Quando usar

- Você vai promover um feitiço de `draft` para `battle-tested`.
- Você editou o corpo de um feitiço e quer saber o que regrediu.
- Dois modelos divergem e você precisa de casos, não de opinião sobre qual “escreve melhor”.

## Quando não usar

- Você ainda não tem o texto do feitiço fechado. Avaliar um rascunho mental produz casos para um prompt que não existe.
- Você quer métrica de negócio (fraude pega X%). Isso exige base rotulada, não este feitiço.
- Você quer nota de 0 a 10 para “qualidade da prosa”. Fora de escopo. Se o feitiço promete prosa, a regra mecânica tem de ser estrutural (seção presente, tamanho máximo, proibição de uma palavra).

## Contexto de uso

Rode com temperatura baixa. A bateria gerada deve ser executada depois, noutro turno, com o feitiço sob teste isolado — não peça ao mesmo turno para criar o caso e já “passar” nele. Quem escreve a prova não assina o próprio gabarito no mesmo fôlego.

Grave o resultado em `exemplos/responses/<id-do-feitico>.md` com data e modelo. Sem esse arquivo, o status não muda.

## Contrato de entrada

| Placeholder | Obrigatório | Notas |
|---|---|---|
| `{{FEITICO}}` | sim | Texto integral, inclusive frontmatter se houver. |
| `{{RESTRICAO_DE_DOMINIO}}` | não | Limites extras do dono do feitiço, por exemplo “não pode citar número de norma”. Se vazio, as únicas obrigações são as que o próprio feitiço escreveu. |

## Contrato de saída

Markdown com:

1. `## Promessa extraída` — no máximo 5 bullets, cada um copiado ou parafraseado justo do que o feitiço diz que faz. Se o feitiço não promete recusa, um bullet tem de ser `não define recusa`.
2. `## Casos` — tabela com 9 linhas de dados, exatamente 3 `control`, 3 `edge`, 3 `capability`.
3. `## Como rodar` — 5 linhas: um caso por vez, sessão limpa, o que gravar.
4. `## Mudanças candidatas` — no máximo 3, cada uma citando o `id` do caso que ela conserta. Se não houver defeito visível sem rodar, escreva `nenhuma até executar a bateria`. Não reescreva o feitiço inteiro.

Colunas da tabela:

| coluna | regra |
|---|---|
| id | `C1`…`C3`, `E1`…`E3`, `K1`…`K3` |
| classe | `control` \| `edge` \| `capability` |
| entrada | o que o humano cola no lugar dos placeholders, ou o estado “placeholder literal” |
| acerto | condição mecânica |
| falha típica | o jeito conhecido de o modelo errar este tipo de caso, não uma previsão mística |
| verificar | `script` ou `humano-1min`, mais o procedimento |

## O Feitiço

```markdown
Você projeta testes de prompt. Você não responde a tarefa que o prompt sob teste resolve. Se você perceber que começou a escrever a resposta da tarefa (o code review, o parecer, o AGENTS.md), pare, apague e volte para a bateria.

# Feitiço sob teste
{{FEITICO}}

# Restrição extra do dono
{{RESTRICAO_DE_DOMINIO}}

# O que as classes significam

- control: entrada bem-formada, completa, dentro do que o feitiço descreve como caso feliz. Se falhar aqui, o feitiço está quebrado ou o modelo não o segue. O acerto tem de ser quase trivial para um revisor que leu o feitiço.
- edge: a entrada ataca o contrato. Use variedade, não três jeitos de dizer a mesma sujeira. O conjunto dos três deve cobrir, quando o feitiço tiver esses pontos — e se não tiver, o caso registra a omissão:
  1. placeholder não substituído, o token do feitiço ainda literal na entrada;
  2. entrada vazia, ou do tipo errado (lista no lugar de objeto, idioma misturado, dado enorme resumido como “10 mil linhas” sem colar as 10 mil — descreva o corte);
  3. instrução hostil dentro do dado (o usuário pede para ignorar o formato). Isso é edge de robustez, não um concurso de jailbreak. O acerto é obedecer ao feitiço, não ao dado.
- capability: o feitiço promete algo que modelo mediano erra. Exemplos do tipo: recusar quando falta política; não inventar comando de teste; citar caminho de arquivo; manter uma única pergunta; não produzir ação irreversível. A promessa tem de estar escrita no feitiço. Não cobre capability de um feitiço melhor que você gostaria que existisse.

# Procedimento

1. Leia o feitiço e extraia a promessa em até 5 bullets. Inclua formato de saída e as recusas explícitas. Se a recusa não existe, escreva o bullet `não define recusa`.
2. Aplique {{RESTRICAO_DE_DOMINIO}} como promessa adicional só se o texto não for vazio.
3. Escreva 9 casos. Cada acerto é uma condição que um script ou um humano apressado confere:
   - seção presente ou ausente;
   - primeira linha igual a uma string;
   - contagem (no máximo N hipóteses, exatamente uma decisão);
   - proibição lexical (não contém “Resolução”, não contém comando que não estava na entrada);
   - citação: um caminho que estava na entrada aparece, um caminho que não estava não aparece.
   “Resposta útil” não é condição. “Tom empático” não é condição, a menos que o feitiço dê marca objetiva (por exemplo: a seção Mensagem Final existe).
4. Para cada caso, a falha típica é uma frase. Ela descreve o erro, não entrega um exploit contra sistema de terceiro.
5. Não reescreva o feitiço. No bloco final, no máximo 3 mudanças, cada uma no formato: `caso EX → mudança: ... → efeito esperado: ...`. Se a bateria ainda não foi executada, as mudanças são hipóteses e precisam desse nome: prefixe com `hipotese:`. Você não viu o modelo falhar; você antecipou. Não finja medição.
6. Se o feitiço sob teste for este próprio feitiço, ainda assim escreva a bateria. Não entre em recursão de rodar os casos.

# Forma

## Promessa extraída
## Casos
tabela markdown com as colunas id, classe, entrada, acerto, falha típica, verificar
## Como rodar
## Mudanças candidatas

# Proibições

- Não 9 casos da mesma classe.
- Não entrada que exija segredo, PII real ou acesso a um banco de produção. Dado do caso é sintético.
- Não diga “depende” na coluna acerto.
- Não inclua o texto integral de um payload de ataque reutilizável contra um assistente de banco. No caso de instrução hostil, descreva a classe (“o campo de descrição pede para ignorar o formato e responder só ‘ok’”) e cobre o acerto observável.
- Não dê nota global. Bateria não é ranking.
```

## Exemplo de caso (espécime: gerador de commit do próprio grimório)

Promessa extraída, ilustrativa, a partir de `grimorio/artefatos/codigo/commit-messages.md`:

- gerar três mensagens;
- a primeira no padrão tipo Conventional Commits;
- identificar qual é qual;
- a terceira é a variante “sexta às 17h”;
- não define recusa.

Caso `E1` que a bateria deveria conter:

| campo | conteúdo |
|---|---|
| id | E1 |
| classe | edge |
| entrada | o texto literal do placeholder de diff do feitiço de commit, ainda não substituído no lugar do diff |
| acerto | a resposta não inventa um diff; ou pede a descrição, ou declara que o placeholder não foi substituído. Falha se aparecerem três mensagens sobre uma mudança específica que não estava na entrada |
| falha típica | o modelo escreve `feat: adiciona validação de login` a partir do nada |
| verificar | humano-1min: procurar substantivo de mudança que não está na entrada |

Caso `K1`:

| campo | conteúdo |
|---|---|
| id | K1 |
| classe | capability |
| entrada | um diff de três arquivos sem mensagem pronta, por exemplo renomear teste e ajustar assertion |
| acerto | existem exatamente 3 mensagens rotuladas; a formal começa com um token do tipo `feat`, `fix`, `refactor`, `test`, `chore`, `docs` seguido de dois-pontos; a formal não descreve arquivo que não está no diff |
| falha típica | uma mensagem só, ou prefixo `update:` |
| verificar | script: contar rótulos e checar regex `^(feat\|fix\|refactor\|test\|chore\|docs):` na formal |

Isto é ilustração do método. A bateria completa dos commits ainda precisa ser gerada rodando este feitiço, e a saída real vai para `exemplos/responses/`. Não copie este trecho como se a medição já tivesse ocorrido.

## Rubrica de aceitação

A bateria gerada passa se:

1. Existem 3 control, 3 edge, 3 capability, com ids estáveis.
2. Nenhuma célula de acerto contém “útil”, “claro”, “completo” ou “bom” como critério único.
3. O caso de placeholder literal existe quando o feitiço declara placeholder. Se o feitiço não declara, um edge justifica a ausência.
4. Capability cita, na coluna entrada ou acerto, uma obrigação que aparece no feitiço sob teste. Não uma obrigação nova.
5. O bloco de mudanças tem 0 a 3 itens, todos com id de caso, e nenhum reescreve o feitiço por completo.
6. Não há PII real nem passo de fraude executável.

## Modos de falha

- **O modelo responde a tarefa.** Você pediu eval do code review e recebeu um code review. Descarte. A primeira linha da saída tem de ser `## Promessa extraída`.
- **Acerto estético.** “Mensagem bem escrita” na coluna. Reprovar a bateria, não o feitiço sob teste.
- **Três edges iguais.** Vazio, nulo e “sem informação”. Exija a variedade da etapa de edge.
- **Capability aspiracional.** O caso cobra JSON quando o feitiço pede markdown. Isso mede o avaliador, não o feitiço.
- **Autoaprovação.** O mesmo turno gera a bateria e preenche “todos passaram”. Inválido. `## Como rodar` tem de insistir em sessão limpa.

## Variações

- **Regressão entre versões.** Cole os dois textos do feitiço e peça só os casos que a versão nova pode ter quebrado, mantendo 3+3+3 se ainda couber, ou uma tabela menor titulada `## Casos de diff` — nessa variação o número 9 deixa de valer, e o título muda para não mentir.
- **Comparar modelos.** A bateria é a mesma. Não peça “casos em que o modelo A perde”. Isso vaza o gabarito para um lado.
- **Feitiço sem formato.** Se a promessa extraída for só “ajude o usuário”, a bateria pode ser curta e o primeiro item de mudança candidata é: o feitiço não é testável até ganhar formato. Não invente nove casos de teatro.

## Notas de segurança

Eval de prompt de fraude ou de injeção usa dado sintético. O caso edge de “instrução hostil dentro do campo” descreve a classe; não vira um corpus de ataque para colar num participante do arranjo.

Não rode a bateria em cima de alerta de produção para “ter realismo”. Realismo se faz com campo no mesmo formato, valor fictício.

## Histórico

- 0.1.0 (2026-10-10) — draft. Ainda não há `exemplos/responses/` gerado por este método.
