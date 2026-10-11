---
id: agents-md-harness
titulo: Harness AGENTS.md a partir do repositório
camara: arquivos-de-contexto/sistema
categoria: harness
objetivo: Produzir um AGENTS.md que outro agente execute sem inventar comando, arquitetura ou regra aspiracional.
entrada: [arvore e trechos, comandos verificados, limites do produto]
saida: markdown
placeholders: ["{{ARVORE_E_TRECHOS}}", "{{COMANDOS_VERIFICADOS}}", "{{LIMITES_DO_PRODUTO}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: nenhum
proveniencia: original
fonte: ""
substitui: ""
---

# Harness AGENTS.md a partir do repositório

## Objetivo

Gerar o arquivo `AGENTS.md` (ou `AGENT.md`) de um repositório real. O leitor é outro modelo, numa sessão futura, sem a sua memória. O arquivo tem de caber na cabeça desse modelo e impedir o estrago típico: refatorar o que não foi pedido, inventar script de teste, e tratar desejo do README como se fosse comportamento do código.

## Quando usar

- O repositório já tem código e pelo menos um jeito conhecido de compilar ou testar.
- Você vai colar árvore, trechos e uma lista curta de comandos que um humano rodou.
- O destino é um agente de código (Copilot, Cursor, Claude Code, Grok, outro) que lê instrução de repositório no começo da sessão.

## Quando não usar

- Você não leu o repo e quer um `AGENTS.md` “genérico de .NET”. Isso produz regra aspiracional. Recuse.
- O que você precisa é de instrução de produto para o usuário final. Isso é README.
- O que você precisa é o contrato de uma ferramenta MCP. Use `contrato-ferramenta-mcp`.
- O que você precisa é o loop do agente (quando chamar ferramenta, quando parar). Use `loop-agente-com-ferramentas`. Este feitiço escreve a política do repositório, não o loop.

## Contexto de uso

Funciona melhor em modelo com janela grande, temperatura baixa (0 a 0.3). Cole a árvore truncada de propósito: profundidade 3, sem `bin/`, `obj/`, `node_modules/`, `.git/`. Cole trechos só dos arquivos que provam uma regra. Se o comando não foi executado, não o inclua em `{{COMANDOS_VERIFICADOS}}`.

## Contrato de entrada

| Placeholder | Obrigatório | Formato |
|---|---|---|
| `{{ARVORE_E_TRECHOS}}` | sim | Árvore em texto mais blocos `path` + conteúdo. Marque o que foi omitido. |
| `{{COMANDOS_VERIFICADOS}}` | sim | Lista. Cada item: comando, diretório, o que apareceu de sucesso, data aproximada. Lista vazia é válida e deve produzir a seção “não verificado”. |
| `{{LIMITES_DO_PRODUTO}}` | não | O que o dono do repo declarou que o sistema não faz. Se vier vazio, o feitiço não inventa limite de negócio; só limites observados no código. |

## Contrato de saída

Um único documento markdown, pronto para gravar como `AGENTS.md`. Sem preâmbulo do tipo “claro, aqui está”. Sem crase envolvendo o arquivo inteiro. Máximo de 120 linhas. Seções, nesta ordem, com estes títulos literais:

1. `## O que é`
2. `## O que não é`
3. `## Mapa`
4. `## Regras invioláveis`
5. `## Verificar uma mudança`
6. `## Fora de escopo`
7. `## Quando a tarefa for ambígua`
8. `## Lacunas`

`## Lacunas` lista o que não deu para afirmar a partir da entrada. Lacuna não é defeito do feitiço; é o oposto de inventar.

## O Feitiço

```markdown
Você escreve harness de agente para um repositório de software. Sua saída será lida por outro modelo, sozinho, meses depois, sem esta conversa. Escreva para esse leitor. Não escreva para me agradar.

Eu não quero um guia de boas práticas. Eu quero um conjunto de restrições que um agente consiga obedecer ou violar de forma óbvia. Regra que não dá para violar de propósito (“seja limpo”, “trate erros”, “escreva testes”) é decoração e está proibida.

# Material

Árvore e trechos (única fonte de arquitetura):
{{ARVORE_E_TRECHOS}}

Comandos que um humano executou (única fonte de verificação):
{{COMANDOS_VERIFICADOS}}

Limites declarados pelo dono, se houver:
{{LIMITES_DO_PRODUTO}}

# Procedimento interno, nesta ordem

Não mostre este procedimento na saída. Execute e entregue só o AGENTS.md.

1. Liste os fatos que estão escritos no material. Fato é o que um terceiro conferiria abrindo o arquivo citado. “Parece um monólito” não é fato. “`src/Pagamentos/PixWorker.cs` consome a fila `pix.liquidacao`” é fato, se o trecho mostrar isso.

2. Liste as tentações. Coisas que um agente mediano faria neste repo e que o material não autoriza. Exemplos do tipo, não uma lista fixa: trocar biblioteca, introduzir camada hexagonal que não existe, criar projeto de teste novo, mudar alvo de framework, reformatar a solução inteira, adicionar autenticação, “modernizar” controller para minimal API.

3. Separe comando verificado de comando plausível. Plausível não entra na seção de verificação. Entra em Lacunas, numa linha: “não verificado: `dotnet test`”.

4. Escreva as regras invioláveis. Cada regra tem as quatro partes na mesma frase ou no mesmo item:
   - o verbo no imperativo negativo ou positivo (“não adicione”, “mantenha”);
   - o arquivo ou diretório que evidencia a regra;
   - o que conta como violação;
   - o que fazer em vez disso, se houver alternativa já presente no repo.
   Teto de 8 regras. Se você tiver 9, descarte a mais genérica.

5. Escreva “fora de escopo” com caminhos concretos. “Não refatore à toa” não serve. “Não mova tipos de `src/Dominio` para um projeto novo” serve, se esse diretório existe.

6. Ambiguidade: uma pergunta, não um palpite. Diga ao agente futuro para parar e perguntar quando a tarefa puder ser lida de dois jeitos e o material não desempatar. Dê dois exemplos de pergunta boa usando nomes deste repo, e um exemplo de pergunta ruim (“posso melhorar o código?”).

7. Conte as linhas. Se passar de 120, corte exemplo antes de cortar regra. Nunca corte a seção Lacunas para “ficar mais confiante”.

# Forma da saída

Títulos literais, nesta ordem: O que é; O que não é; Mapa; Regras invioláveis; Verificar uma mudança; Fora de escopo; Quando a tarefa for ambígua; Lacunas.

- `O que é`: no máximo 5 linhas. Diz o que o código faz com sujeito e verbo. Cita o diretório que concentra esse comportamento.
- `O que não é`: limites observados ou declarados. Se o dono não declarou nenhum, escreva só o que o código contradiz (por exemplo: não há pasta `infra/`, então não descreva o repo como plataforma de infraestrutura).
- `Mapa`: tabela com três colunas — caminho, responsabilidade em uma linha, arquivo-âncora. No máximo 8 linhas. Não liste pasta vazia de asset.
- `Regras invioláveis`: lista numerada, no formato da etapa 4.
- `Verificar uma mudança`: só comandos de {{COMANDOS_VERIFICADOS}}. Para cada um: o comando, o diretório, o sinal de sucesso (texto ou exit code que o humano viu), o sinal de falha. Se a lista vier vazia ou disser “nenhum”, a seção inteira é: “Nenhum comando foi verificado pelo humano. Não invente `dotnet test`, `npm test` nem pipeline. Pergunte.”
- `Fora de escopo`: bullets com caminho.
- `Quando a tarefa for ambígua`: a política de uma pergunta, mais os dois exemplos bons e o ruim.
- `Lacunas`: bullets. Cada uma começa com “não dá para afirmar:”.

# Proibições

- Não invente versão de runtime, nome de projeto, nome de fila, porta, variável de ambiente ou passo de CI.
- Não copie regra de outro ecossistema porque “.NET costuma”. Se o material for Node, as regras são de Node.
- Não elogie o repositório. Não peça desculpa. Não explique o que é um AGENTS.md.
- Não embrulhe a saída em bloco de código.
- Se {{ARVORE_E_TRECHOS}} estiver vazio ou for só um README promocional sem código, não escreva o AGENTS.md. Responda apenas: “material insuficiente: falta árvore ou trecho de código” e pare.
- Se um trecho contradizer outro, não escolha o que “parece mais novo”. Registre a contradição em Lacunas e não transforme nenhum dos dois em regra inviolável.
```

## Exemplo

Entrada resumida (repositório fictício `fits-pix-callback`, recorte):

```text
src/
  Fits.Pix/Fits.Pix.csproj
  Fits.Pix/Worker.cs          # BackgroundService, fila "pix.callback"
  Fits.Pix/CallbackHandler.cs # exige header X-Correlation-Id; sem ele responde 400 via ProblemDetails
test/
  Fits.Pix.Tests/CallbackHandlerTests.cs
Comandos verificados:
- dotnet test test/Fits.Pix.Tests -c Release | exit 0 | 2026-10-01 | na raiz
Limites do produto: não liquida Pix; só recebe callback do provedor.
```

Trecho que a regra precisa citar: `CallbackHandler` devolve 400 quando o header falta. Isso vira regra. “Adicionar MediatR” entra em fora de escopo porque não há MediatR no material.

Saída esperada, formato (trecho, não o arquivo inteiro):

```markdown
## O que é
Serviço .NET que recebe callback de um provedor e o trata em `Fits.Pix/CallbackHandler.cs`, com um worker em `Fits.Pix/Worker.cs` lendo a fila `pix.callback`. Não inicia pagamento.

## O que não é
Não liquida Pix e não é o provedor de conta. Não há pasta de infraestrutura neste repositório.

## Regras invioláveis
1. Não aceite callback sem `X-Correlation-Id`. Violação: mudar `CallbackHandler` para seguir sem o header. Evidência: `Fits.Pix/CallbackHandler.cs`. No lugar disso, mantenha a resposta 400 com ProblemDetails.

## Verificar uma mudança
- `dotnet test test/Fits.Pix.Tests -c Release` na raiz. Sucesso: exit 0. Falha: exit diferente de 0. Não há outro comando verificado.

## Lacunas
- não dá para afirmar: como a fila `pix.callback` é publicada; o trecho só mostra o consumo.
```

O que reprova esta saída: inventar `docker compose up`, exigir cobertura de 80%, ou afirmar que o worker usa MassTransit sem o `csproj` ou o `using` no material.

## Rubrica de aceitação

Confira sem julgar estilo:

1. Os oito títulos existem, na ordem, literais.
2. Nenhuma regra deixa de citar um caminho que estava na entrada.
3. Nenhum comando fora de `{{COMANDOS_VERIFICADOS}}` aparece em “Verificar uma mudança”.
4. Existe pelo menos uma linha em Lacunas, ou a entrada era completa o bastante para o modelo dizer “lacunas: nenhuma além do que a entrada já marcou como omitido” — e nesse caso a omissão tem de estar na entrada.
5. Contagem de linhas ≤ 120.
6. Entrada vazia produz exatamente a frase de recusa, sem AGENTS.md.
7. Não há adjetivo de qualidade (“robusto”, “limpo”, “moderno”) nas regras.

## Modos de falha

- **README como arquitetura.** O modelo descreve o produto do marketing e ignora o worker. Correção: a entrada deve trazer trecho, e a rubrica 2 pega regra sem caminho. Se ainda passar, a árvore estava sem código; o feitiço deveria ter recusado.
- **Comando plausível.** Aparece `dotnet format` ou `npm run lint` porque o ecossistema “sempre tem”. Rubrica 3.
- **Regra gêmea da aspiração.** “Sempre escreva teste” sem apontar o projeto de teste existente. Rubrica 7 e a etapa 4.
- **Arquivo enorme.** O modelo explica cada pasta. Cortar exemplo, não lacuna. Se o usuário precisa de mapa completo, isso é outro documento, não harness.
- **Contradição escondida.** Dois trechos divergem e o modelo escolhe um. Tem de ir para Lacunas.

## Variações

- **`AGENTS.md` já existe.** Cole o atual no fim de `{{ARVORE_E_TRECHOS}}` sob o título `AGENTS.md vigente`. Acrescente na etapa 4: preserve a regra antiga que ainda tem evidência no código; apague a que não tem, e liste a remoção em Lacunas como “removida por falta de evidência: …”. Não faça merge mudo.
- **Monorepo.** Uma saída por aplicação, não um harness gigante. O mapa tem no máximo 8 linhas de propósito. Se houver 6 serviços, rode o feitiço 6 vezes com a árvore recortada, mais um harness curto da raiz que só diz qual pasta é qual e proíbe mudar duas de uma vez sem pedido explícito.
- **Sem teste.** Válido. A seção de verificação fica na forma “nenhum comando foi verificado”. Não crie projeto de teste dentro do AGENTS.md.

## Notas de segurança

O material colado pode conter segredo. Antes de colar, tire connection string, chave e token. O feitiço não tem como adivinhar que um GUID no trecho é credencial. Se um segredo aparecer na saída, a falha foi da entrada; mesmo assim, se você reconhecer padrão de segredo na saída (`AccountKey=`, `BEGIN PRIVATE KEY`, `password=`), não grave o arquivo: volte e peça para o modelo reemitir com o valor substituído por REMOVIDO.

Não use este feitiço para esconder política de compliance dentro do harness. Norma regulatória pertence a `pix-contexto-injetavel` ou a um contexto de negócio, com fonte primária. Misturar as duas coisas faz o agente citar artigo que ninguém colou.

## Histórico

- 0.1.0 (2026-10-10) — versão inicial, draft, sem modelo testado.
