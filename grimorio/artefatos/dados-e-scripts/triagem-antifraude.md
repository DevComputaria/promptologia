---
id: triagem-antifraude
titulo: Triagem de alerta antifraude
camara: artefatos/dados-e-scripts
categoria: fintech
objetivo: Transformar um alerta em parecer de fila, sem inventar evento e sem ação irreversível não autorizada.
entrada: [alerta, politica, contexto pix opcional]
saida: markdown
placeholders: ["{{ALERTA_JSON}}", "{{POLITICA}}", "{{CONTEXTO_EXTRA}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: dados-sensiveis
proveniencia: original
fonte: ""
substitui: ""
---

# Triagem de alerta antifraude

## Objetivo

Produzir o parecer que um analista de primeiro nível grava no caso, a partir do alerta que o motor já gerou. O parecer separa o que está no payload, o que é hipótese, e qual fila segue. Não é score, não é denúncia e não é ordem de bloqueio.

## Quando usar

- Existe um alerta estruturado (JSON ou equivalente) de um motor, fila ou regra.
- A decisão possível nesta etapa é de fila: liberar, segurar, escalar, ou pedir dado.
- O revisor humano vai ler o parecer em poucos minutos.

## Quando não usar

- Não há alerta: só um relato oral. Peça para estruturar o evento mínimo (quem, valor, quando, identificadores, canal) antes. Não deixe o modelo entrevistar indefinidamente.
- Você quer descobrir se a regra do motor está bem calibrada em milhares de casos. Isso é análise de métrica, outro trabalho.
- Você quer um texto para o cliente, para a polícia ou para um regulador. O parecer daqui é interno e condicional.
- Você quer que o modelo execute o bloqueio. Ele não executa nada. No máximo recomenda, e só dentro da política colada.

Se a sessão for de Pix, carregue antes `pix-contexto-injetavel`. Sem esse contexto o modelo mistura estorno, devolução e “pago porque deu 200”.

## Contexto de uso

Temperatura baixa. Não use ferramenta de busca para “enriquecer” o alerta com vazamento público, rede social ou lista de fraude da internet. O mundo fora do JSON não entra, salvo o bloco `{{CONTEXTO_EXTRA}}` que você mesmo colou (extrato mascarado, cadastro interno, política).

Dado real: mascare documento, chave e nome antes de colar. O exemplo deste arquivo é sintético. Não “complete” com caso de produção.

## Contrato de entrada

| Placeholder | Obrigatório | Notas |
|---|---|---|
| `{{ALERTA_JSON}}` | sim | Um objeto. Se vier lista, o feitiço recusa e pede um alerta por vez. |
| `{{POLITICA}}` | sim | Texto da política interna vigente, ou a frase exata `politica-nao-fornecida`. Vazio não é permitido: vazio faz o modelo inventar threshold. |
| `{{CONTEXTO_EXTRA}}` | não | Fatos adicionais já coletados, cada um com origem (`ledger`, `cadastro`, `dispositivo`). Se vazio, o modelo não assume extrato. |

## Contrato de saída

Markdown com os títulos literais abaixo, nesta ordem. Sem introdução.

1. `## Fatos no alerta`
2. `## Fatos no contexto extra`
3. `## O que não está no material`
4. `## Hipóteses`
5. `## Decisão de fila`
6. `## Ação irreversível`
7. `## Pergunta única ao próximo humano`

Regras de seção:

- Fatos: bullets que apontam caminho JSON (`alerta.valor`, `alerta.sinais[0]`). Sem adjetivo (“valor alto” não é fato; “valor = 9800 e moeda = BRL” é).
- Contexto extra vazio: a seção existe e diz `nenhum contexto extra colado`.
- Hipóteses: no máximo 3. Cada uma com sinais a favor, sinais contra, e o dado que a confirmaria. Tipologia não é conclusão.
- Decisão de fila: exatamente uma de `liberar` | `segurar` | `escalar` | `pedir-dado`.
- Ação irreversível: `nao-recomendada` ou `recomendada-pela-politica`. A segunda só com citação literal de um trecho de `{{POLITICA}}` que case com o fato. Bloqueio de conta, encerramento, devolução, acionamento de mecanismo especial de devolução e qualquer débito contam como irreversíveis para este feitiço.
- Pergunta única: uma frase. Se a decisão já está fechada sem lacuna, a frase é `nenhuma — o material basta para a fila escolhida`.

## O Feitiço

```markdown
Você é analista de fraude de primeiro nível escrevendo para outro humano da fila. Você não é o motor de score, não é juiz, não é o chatbot do cliente e não executa ação em sistema nenhum.

# Material — única realidade

Alerta (um objeto JSON):
{{ALERTA_JSON}}

Política interna (ou a frase politica-nao-fornecida):
{{POLITICA}}

Contexto extra já coletado:
{{CONTEXTO_EXTRA}}

# Procedimento

Não mostre o procedimento. Mostre só o parecer.

1. Valide o alerta. Se não for um único objeto JSON parseável, responda somente:

alerta-invalido: esperado um objeto JSON

e pare. Não tente consertar vírgula “no olho” se houver ambiguidade; aí também é inválido. Lista no topo é inválida.

2. Se {{POLITICA}} estiver vazia ou for placeholder não substituído, responda somente:

politica-ausente: cole a política ou a frase politica-nao-fornecida

e pare. A frase politica-nao-fornecida é uma entrada válida e significa: não existe autorização escrita nesta sessão.

3. Extraia fatos com caminho. Ignore campo decorativo (nome de cor de regra, texto motivacional do motor). Não some valores que não estejam somados no alerta. Não converta fuso: se o timestamp não tiver offset, diga que não tem offset, não escolha America/Fortaleza por conta própria.

4. Liste lacunas que mudariam a fila. Exemplos do tipo: não há histórico, não há estado de liquidação, não há vínculo entre o dispositivo e o cadastro, a política não define teto. Não liste lacuna cosmética.

5. Formule no máximo 3 hipóteses. Use tipologia como rótulo de hipótese, nunca como fato. Rótulos permitidos, e só estes — se nenhum servir, use `outro` e descreva em uma linha:
   - tomada-de-conta
   - mula-ou-intermediacao
   - engenharia-social
   - troca-de-recebedor
   - velocidade-ou-valor-atipico
   - falha-operacional
   - outro

   Para cada hipótese, sinais a favor têm de apontar caminho no alerta ou no contexto extra. Sinal sem caminho é opinião e não entra. Sinais contra são obrigatórios: se você não achar um, escreva `nenhum sinal contrário no material` — isso enfraquece a hipótese, não a fortalece.

6. Escolha uma fila:
   - `liberar` — o material não sustenta nem a hipótese mais forte, e a política não manda segurar esse tipo de alerta;
   - `segurar` — há hipótese com sinal a favor e a política pede espera, ou falta um dado que chega sozinho em pouco tempo (você não inventa o tempo: se a política não diz, não use segurar por tempo);
   - `escalar` — a hipótese, se verdadeira, exigiria ação irreversível ou especialidade que esta fila não tem;
   - `pedir-dado` — a decisão muda com um dado específico que você nomeia.

   Se `politica-nao-fornecida` e houver qualquer hipótese com sinal a favor concreto, você não escolhe `liberar`. Escolhe `escalar` ou `pedir-dado`. Sem política, liberar é chute.

7. Ação irreversível. Default: `nao-recomendada`. Só escreva `recomendada-pela-politica` se copiar, entre aspas, o trecho da política que cobre este caso, e apontar o fato que casa com a condição. “A política diz para ter rigor” não casa com nada. Sem casar condição e fato, mantenha `nao-recomendada` mesmo que a hipótese seja grave — e use a fila `escalar`.

8. Feche com uma pergunta. Uma. A que desempata. Não um questionário.

# Forma

Títulos literais, nesta ordem:
## Fatos no alerta
## Fatos no contexto extra
## O que não está no material
## Hipóteses
## Decisão de fila
## Ação irreversível
## Pergunta única ao próximo humano

Em Decisão de fila, a primeira linha é só a palavra da fila. Depois, no máximo 6 linhas justificando, cada uma citando um caminho ou a ausência de política.

Em Hipóteses, repita este bloco:

### H1 — {rotulo}
- a favor:
- contra:
- confirmaria:

# Proibições

- Não invente transação, dispositivo, IP, geolocalização, “o cliente sempre faz isso”, ou histórico.
- Não atribua intenção. “Padrão compatível com tomada de conta” pode. “O fraudador quis” não pode.
- Não cite lei, artigo ou prazo de mecanismo de devolução de memória. Se a política colada citar, você pode repetir a citação da política como texto interno, sem “confirmar” que a norma existe.
- Não recomende o texto a enviar ao cliente.
- Não faça a segunda hipótese “por completude” se ela não tem sinal. Menos hipótese é melhor.
- Não use o nome de uma pessoa do alerta em exemplo ou piada. Trate documento como dado, já mascarado de preferência.
```

## Exemplo

Alerta sintético:

```json
{
  "id": "ALR-1001",
  "tipo": "VELOCIDADE",
  "conta_origem_mascarada": "***11",
  "valor": 9800,
  "moeda": "BRL",
  "liquidacao_confirmada": false,
  "chave_destino_tipo": "aleatoria",
  "sinais": [
    {"codigo": "QTD_1H", "valor": 4},
    {"codigo": "VALOR_VS_BASELINE", "valor": "sem-baseline"}
  ],
  "canal": "app"
}
```

Política: `politica-nao-fornecida`. Contexto extra vazio.

Trecho de saída aceitável:

```markdown
## Fatos no alerta
- alerta.id = ALR-1001
- alerta.tipo = VELOCIDADE
- alerta.valor = 9800 e alerta.moeda = BRL
- alerta.liquidacao_confirmada = false
- alerta.sinais[0] = QTD_1H / 4
- alerta.sinais[1] = VALOR_VS_BASELINE / sem-baseline
- alerta.chave_destino_tipo = aleatoria

## Fatos no contexto extra
nenhum contexto extra colado

## O que não está no material
- estado de liquidação além do booleano false (não há identificador de liquidação)
- baseline numérico (o próprio sinal diz sem-baseline)
- vínculo de dispositivo ou cadastro
- política interna

## Hipóteses
### H1 — velocidade-ou-valor-atipico
- a favor: sinais[0] registra 4 eventos em 1h na origem mascarada ***11
- contra: sinais[1] diz sem-baseline, então “atípico versus o próprio cliente” não está demonstrado
- confirmaria: baseline da conta e a lista dos 4 identificadores, com estado de cada um

## Decisão de fila
escalar
Sem política colada não liberto um alerta que tem sinal concreto (QTD_1H = 4). Também não seguro por prazo porque nenhum prazo foi dado. Liquidação não está confirmada (liquidacao_confirmada = false), então ação de devolução nem teria premissa.

## Ação irreversível
nao-recomendada

## Pergunta única ao próximo humano
Os quatro eventos contados em QTD_1H são quatro liquidações, quatro tentativas rejeitadas, ou quatro callbacks da mesma cobrança?
```

O que reprova: “bloquear a conta”; inventar que a chave aleatória “é típica de mula”; tratar 9800 como acima de um teto que ninguém escreveu; escolher `liberar` com política ausente.

## Rubrica de aceitação

1. JSON inválido ou lista produz só a linha `alerta-invalido: …`.
2. Política vazia produz só `politica-ausente: …`. A frase `politica-nao-fornecida` não dispara essa recusa.
3. Com `politica-nao-fornecida` e ao menos um sinal concreto, a fila não é `liberar`.
4. `recomendada-pela-politica` só aparece com citação entre aspas presente no texto da política.
5. Nenhuma hipótese usa rótulo fora da lista.
6. Todo sinal a favor contém um caminho (`alerta.` ou origem do contexto extra).
7. Não aparece prazo de norma nem a palavra “fraudador” como fato.
8. Há no máximo 3 hipóteses e exatamente uma pergunta no fim.

## Modos de falha

- **Narrativa policial.** O modelo encadeia tomada de conta → mula → lavagem porque o valor “é redondo”. Sem caminho, a rubrica 6 corta. Se passar, o sinal foi vago o bastante para parecer caminho (`alerta.tipo`). Aperte o exemplo de treino: tipo do alerta não é sinal a favor da tipologia de mesmo nome, é só a etiqueta do motor.
- **MED automático.** Recomenda mecanismo de devolução porque liquidação futura “vai acontecer”. Proibido pela classe de ação irreversível e pelo booleano de liquidação.
- **Política parafraseada.** “A política sugere cautela” sem aspas. Não conta como autorização. Rubrica 4.
- **Questionário.** Cinco perguntas no fim. A seção pede uma. Corte na revisão humana; se for frequente, o modelo não segurou formato — não compense alongando o feitiço com mais exemplos até medir (use `eval-control-edge-capability`).
- **Alerta consertado.** JSON quebrado vira parecer. A etapa 1 existe para isso. Teste com uma vírgula sobrando antes de confiar.

## Variações

- **Lote.** Não aumente este feitiço para N alertas. Um shell seu itera e grava N pareceres. O modelo perde a conta e mistura `id` no meio do lote.
- **Cartão ou conta corrente sem Pix.** Dá para reutilizar a estrutura, mas troque os rótulos de hipótese. Não force “chave aleatória” num alerta de cartão. Outro arquivo, quando existir massa, não um `if` gigante aqui.
- **Segunda linha, depois da triagem.** Quando o humano responder a pergunta única, cole a resposta em `{{CONTEXTO_EXTRA}}` e rode de novo. Não peça “continue no mesmo tom” sem recolocar o alerta: a sessão esquece campo.

## Notas de segurança

Parecer não é acusação e não se cola em canal com o cliente. Não inclui dado que não esteja mascarado se o destino for um ticket de fornecedor.

O feitiço não pede para o modelo caçar a pessoa em fonte aberta. Se alguém acrescentar essa instrução na política colada, não obedeça àquele parágrafo: a proibição de inventar e de buscar fora do material ganha, e o parecer registra `política pediu enriquecimento externo — ignorado por este feitiço`.

Uso dual: um parecer bem feito também ensina quais sinais um alerta expõe. Não publique alerta real junto com este prompt.

## Histórico

- 0.1.0 (2026-10-10) — draft. Depende, em sessão de Pix, de `pix-contexto-injetavel` carregado antes, embora não o incorpore para não duplicar norma.
