---
id: few-shot-cot-autocritica
titulo: Few-shot, cadeia de pensamento e autocrítica
camara: tecnicas
categoria: harness
objetivo: Ensinar quando acrescentar exemplo, raciocínio e revisão, usando o gerador de commit como espécime.
entrada: [feitico base, sintomas opcionais]
saida: markdown
placeholders: ["{{FEITICO_BASE}}", "{{SINTOMA}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: nenhum
proveniencia: original
fonte: ""
substitui: ""
---

# Few-shot, cadeia de pensamento e autocrítica

## Objetivo

Decidir qual acréscimo um feitiço precisa, e escrever só esse acréscimo. As três técnicas não são um combo obrigatório. Empilhar as três “para ficar mais inteligente” gasta contexto e às vezes piora o formato, porque o modelo passa a imitar o raciocínio do exemplo em vez da saída.

Espécime fixo deste arquivo: o feitiço de mensagens de commit em `grimorio/artefatos/codigo/commit-messages.md`. Os exemplos abaixo usam esse espécime para a técnica ficar concreta. Quando você aplicar a técnica a outro feitiço, troque o espécime; não deixe o modelo devolver mensagens de commit se a tarefa era outra.

## Quando usar

- O feitiço já tem objetivo e formato, e ainda erra de um jeito que você consegue nomear (`{{SINTOMA}}`).
- Você tem pelo menos um par entrada → saída correta, escrito por humano, para few-shot. Sem par correto, few-shot vira few-shot do erro.
- A saída é estruturada o bastante para a autocrítica ter checklist, não “veja se ficou bom”.

## Quando não usar

- O feitiço não tem formato. Técnica nenhuma conserta “me ajude”. Volte ao `meta-prompt-template.md`.
- Você quer medir se melhorou. Medição é `eval-control-edge-capability`. Esta técnica só propõe o acréscimo; quem promove versão é a bateria, em sessão separada.
- O sintoma é fato inventado de domínio (prazo de Pix, comando que não existe). Exemplo não cura alucinação de conhecimento. Contexto de domínio e proibição explícita curam, ou não curam; few-shot de um caso só empurra o erro para o caso vizinho.

## Contexto de uso

Leia o sintoma antes de escolher a técnica. Mapa usado por este feitiço:

| Sintoma observável | Técnica que entra primeiro | Por que não as outras |
|---|---|---|
| Formato errado, tom errado, esquece uma das N partes | few-shot, 2 exemplos | CoT longo não fixa forma; o modelo explica e continua errando a forma |
| Caso limítrofe classificado mal (qual prefixo de commit, qual fila) | few-shot do limítrofe, não do caso óbvio | O caso óbvio ele já acerta |
| Pulou uma restrição no meio do caminho | cadeia curta, com checklist obrigatório na saída ou fora dela | Few-shot sem o caso da restrição não mostra a restrição |
| Saiu no formato certo e mesmo assim violou uma regra conferível | autocrítica com lista fechada | Pedir “revise” sem lista só deixa a prosa mais longa |
| Tudo isso junto | uma técnica por versão | Três técnicas no mesmo diff impedem saber qual funcionou |

Cadeia de pensamento: se o produto precisa só da resposta final, peça o raciocínio num bloco delimitado e a resposta noutro, e diga qual bloco o usuário vai copiar. Não peça “pense passo a passo” solto no fim: muitos modelos então entregam só o passo a passo.

## Contrato de entrada

| Placeholder | Obrigatório |
|---|---|
| `{{FEITICO_BASE}}` | sim |
| `{{SINTOMA}}` | sim. Uma frase do erro visto, com um exemplo mínimo do que saiu. “Ficou ruim” é inválido. |

## Contrato de saída

1. `## Sintoma classificado` — uma linha, a técnica escolhida, e a técnica que você se recusou a usar.
2. `## Acréscimo` — só o texto novo para inserir no feitiço, com a marca de onde entra (`depois do bloco de formato`, `antes das proibições`). Não reimprima o feitiço inteiro.
3. `## Custo` — o que esse acréscimo pode piorar.
4. `## Como saber se funcionou` — uma condição mecânica, pronta para virar caso `K` na bateria de eval.

Se o sintoma for vago, a saída inteira é: `sintoma-vago: descreva o que saiu e o que deveria ter saído`.

## O Feitiço

```markdown
Você altera prompts com uma técnica por vez. Você não reescreve o feitiço inteiro e não finge que já mediu o resultado.

# Feitiço base
{{FEITICO_BASE}}

# Sintoma visto num modelo, descrito por humano
{{SINTOMA}}

# Escolha

Classifique o sintoma numa destas cestas, uma só:
- formato
- classe-limitrofe
- pulou-restricao
- violou-regra-conferivel
- vago
- conhecimento-inventado

Se vago: responda só `sintoma-vago: descreva o que saiu e o que deveria ter saído` e pare.
Se conhecimento-inventado: responda só `tecnica-errada: exemplo não substitui fonte; acrescente proibição e contexto, não few-shot` e pare.

Mapeamento:
- formato ou classe-limitrofe → escreva few-shot
- pulou-restricao → escreva cadeia curta
- violou-regra-conferivel → escreva autocrítica

Não entregue as três. Se duas cestas parecerem certas, escolha a que está mais acima nesta lista: formato, depois classe-limitrofe, depois pulou-restricao, depois violou-regra. Diga a que você deixou de fora.

# Como escrever cada técnica

## Few-shot
Dois exemplos, não cinco. Cada exemplo tem entrada mínima e saída no formato exato que o feitiço pede. O segundo exemplo é o limítrofe, próximo do sintoma, não uma repetição do primeiro. Dados sintéticos. Não use diff real de cliente.

Marque o bloco:

[EXEMPLOS]
Entrada 1:
...
Saída 1:
...
Entrada 2:
...
Saída 2:
...
[/EXEMPLOS]

Diga para inserir depois da descrição do formato e antes do placeholder da entrada real. Inclua uma linha de instrução: “se a entrada real contradisser o estilo dos exemplos, obedeça às regras do feitiço, não ao exemplo”.

## Cadeia curta
No máximo 5 checagens, numeradas, cada uma com sim ou não, sobre a entrada. Depois um bloco `RESPOSTA` que é a única coisa a copiar. A checagem não pode pedir fato de fora da entrada. Se a checagem for “isso é Conventional Commits?”, diga o critério (prefixo na lista permitida pelo feitiço).

Não escreva um ensaio. Se passar de 5 checagens, você está reescrevendo o feitiço: pare e corte.

## Autocrítica
Uma lista de no máximo 6 itens conferíveis, no imperativo, que o modelo aplica à própria resposta antes de devolvê-la. Cada item tem falha objetiva (“se houver só uma mensagem, reescreva até haver três rotuladas”). Feche com: “se reescrever, entregue somente a versão final, não as duas”.

Não peça “melhore o estilo”. Não peça uma segunda opinião aberta.

# Custo, obrigatório
Diga em duas linhas o que pode piorar. Exemplos do tipo, escolha os que forem verdade para a técnica que você escolheu:
- few-shot: o modelo copia detalhe do exemplo (nome de arquivo, ticket) para a entrada nova;
- cadeia: a resposta final vem vazia e só vêm as checagens;
- autocrítica: a resposta dobra de tamanho e ainda viola a regra, agora com um parágrafo pedindo desculpa.

# Medição
Uma condição mecânica. Sem adjetivo. Essa condição será um caso de eval depois; você não a executa agora.

# Forma da sua saída
## Sintoma classificado
## Acréscimo
## Custo
## Como saber se funcionou
```

## Exemplo no espécime de commit

Sintoma fictício, ainda não medido em `exemplos/responses/` — trate como ilustração de forma, não como regressão registrada:

“O modelo devolveu uma mensagem só, `update: ajusta testes`, sem os três rótulos, para um diff que só muda assertion.”

Cesta: `formato`. Técnica: few-shot. Não usar ainda autocrítica, porque a forma nem apareceu; criticar uma saída que não tem três blocos é o passo seguinte, se o few-shot falhar.

Acréscimo ilustrativo (entra depois do pedido das três versões, antes do placeholder de diff desse feitiço):

```markdown
[EXEMPLOS]
Entrada 1:
diff que adiciona o endpoint GET /saude devolvendo 200 sem corpo novo de negócio
Saída 1:
1. Formal — feat: adiciona endpoint de saude
2. Casual — coloca um /saude que só responde 200
3. Sexta às 17h — espero que ninguém precise disso no feriado
Entrada 2:
diff que só altera a assertion de um teste existente, sem produção
Saída 2:
1. Formal — test: aperta assertion do callback sem header
2. Casual — o teste agora falha se aceitar request sem correlation id
3. Sexta às 17h — mexe em teste às 17h, o que pode dar errado
[/EXEMPLOS]

Se a entrada real contradisser o estilo dos exemplos, obedeça às regras do feitiço, não ao exemplo. Não reuse o endpoint /saude nem o correlation id se eles não estiverem no diff real.
```

Como saber se funcionou: na entrada 2, a resposta contém os três rótulos `Formal`, `Casual` e `Sexta`, e a formal casa com `^test:`.

Custo: o modelo pode enfiar “correlation id” num diff que não tem isso. A linha final do acréscimo existe para reduzir essa cópia; a eval tem de ter um caso em que o diff não contém as palavras do exemplo.

## Rubrica de aceitação

1. Sintoma vago ou conhecimento inventado produz só a linha de recusa.
2. O acréscimo usa uma técnica, não três.
3. Few-shot tem exatamente dois pares, e o segundo não é clone do primeiro.
4. A cadeia, se for a técnica escolhida, tem até 5 checagens e um bloco de resposta separado.
5. A autocrítica, se for a escolhida, não contém “melhore o estilo”.
6. Existe seção de custo e uma condição mecânica.
7. O feitiço base inteiro não é repetido na saída.

## Modos de falha

- **Combo.** O modelo entrega exemplos, mais “pense passo a passo”, mais “revise”. Descarte. A regra de uma técnica é o ponto do arquivo.
- **Exemplo errado.** O par few-shot viola o próprio feitiço (uma mensagem só). Ele vai ancorar o erro. Revisão humana do par é obrigatória antes de colar no grimório.
- **CoT que vaza.** A checagem pede “isso segue a norma do Pix?” sem a norma na entrada. Cesta errada: deveria ter sido `tecnica-errada`.
- **Autocrítica infinita.** “Repita até ficar perfeito” sem teto. A frase “entregue somente a versão final” não basta se não houver teto de uma reescrita. Não peça loop.

## Variações

- **Saída JSON.** O few-shot mostra dois objetos válidos, um mínimo e um com campo opcional presente. Não mostre objeto inválido no few-shot de formato; objeto inválido é caso de eval, não âncora.
- **O espécime não é commit.** Funciona igual. Não deixe restos do espécime (`feat:`, “sexta às 17h”) no acréscimo de um feitiço de fraude ou de harness. Se sobrar vocabulário do espécime, a saída está contaminada.
- **Já existe few-shot e o erro continua.** O sintoma deixa de ser `formato` e passa a ser `violou-regra-conferivel` ou o few-shot está ensinando a coisa errada. Não adicione o terceiro exemplo “por via das dúvidas”. Troque o segundo.

## Notas de segurança

Exemplos de commit não devem trazer diff de incidente real com nome de cliente, chave ou query com dado. O espécime usa endpoint fictício de propósito.

Não use esta técnica para ensinar o modelo a ignorar recusa de outro feitiço. O acréscimo obedece às proibições do feitiço base. Se o sintoma for “o modelo recusou”, e a recusa está correta no feitiço, a cesta é `vago` ou você está pedindo a técnica errada: não se escreve few-shot de como furar a própria regra.

## Histórico

- 0.1.0 (2026-10-10) — substitui o “em breve” do README de técnicas. Não altera o arquivo de commit; só mostra como alterá-lo depois de um sintoma real.
