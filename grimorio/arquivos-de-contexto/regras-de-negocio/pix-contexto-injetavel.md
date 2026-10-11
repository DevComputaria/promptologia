---
id: pix-contexto-injetavel
titulo: Contexto injetável de Pix
camara: arquivos-de-contexto/regras-de-negocio
categoria: fintech
objetivo: Fixar o modelo mental de Pix numa sessão, sem artigo, prazo ou valor decorado.
entrada: [norma opcional colada pelo humano, papel da sessão]
saida: texto
placeholders: ["{{NORMA_COLADA}}", "{{PAPEL_DA_SESSAO}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: dados-sensiveis
proveniencia: original
fonte: ""
substitui: ""
---

# Contexto injetável de Pix

## Objetivo

Este arquivo não pede uma análise, um código ou um parecer. Ele é carregado no início de uma sessão para o modelo parar de misturar Pix com cartão, TED e boleto, e parar de completar lacuna regulatória com número bonito.

A tarefa vem depois, noutro prompt (`triagem-antifraude`, um review de código, um postmortem). Este contexto só vale até você dizer “contexto pix encerrado” ou até a sessão acabar.

## Quando usar

- A tarefa seguinte fala de pagamento instantâneo no Brasil, callback de provedor, chave, QR, devolução, conta de pagamento ou fraude em transação Pix.
- Você quer uma linha de confirmação e silêncio, não um ensaio sobre o Banco Central.

## Quando não usar

- A tarefa é de outro arranjo (cartão, boleto, TED, DOC, débito automático). Não carregue este contexto “por via das dúvidas”: ele puxa vocabulário errado para o problema certo.
- Você quer aconselhamento jurídico, parecer de compliance ou interpretação de norma. Este contexto manda o modelo pedir o trecho, não emiti-lo.
- Você vai colar extrato real, CPF de cliente ou payload de produção. Troque por dado sintético antes. O risco do frontmatter existe por causa do domínio, não porque o feitiço precise de PII.

## Contexto de uso

Cole o feitiço uma vez. Espere a confirmação de uma linha. Só então cole a tarefa. Se a tarefa exigir prazo, teto de valor, artigo ou janela do MED, cole o trecho oficial em `{{NORMA_COLADA}}` na hora — não antes, não de memória, não “você já sabe”.

`{{PAPEL_DA_SESSAO}}` restringe o que o modelo pode sugerir. Valores aceitos: `engenharia`, `operacao`, `produto`, `revisao-de-texto`. Qualquer outro valor, ou vazio, equivale a `engenharia` e deve ser ecoado como premissa, não como escolha silenciosa.

Temperatura baixa. Não precisa de modelo com busca se a norma estiver colada. Se não estiver colada, busca também não autoriza o modelo a citar artigo sem reproduzir o parágrafo que usou — e mesmo assim a preferência deste grimório é o trecho colado pelo humano.

## Contrato de entrada

| Placeholder | Obrigatório | Se ausente |
|---|---|---|
| `{{NORMA_COLADA}}` | não | O modelo declara “norma não colada” e não cita número de resolução, circular, artigo, prazo ou valor. |
| `{{PAPEL_DA_SESSAO}}` | não | Tratar como `engenharia`. |

## Contrato de saída

Na carga: exatamente uma linha.

```text
contexto pix carregado | papel={papel} | norma={colada|nao-colada}
```

Nada mais. Na tarefa seguinte, cada afirmação regulatória ou numérica cai numa destas classes, ditas em voz alta:

- `fato-de-dominio` — está neste contexto e não depende de vigência;
- `fato-da-norma-colada` — citação curta do trecho que você colou, entre aspas, com a identificação que veio no trecho;
- `inferencia` — conclusão a partir do que está na tarefa;
- `lacuna` — o que faltou para decidir.

Se a classe não couber, a frase não entra na resposta.

## O Feitiço

```markdown
Você vai trabalhar numa sessão sobre Pix, o arranjo de pagamento instantâneo do Brasil. Não responda a tarefa nenhuma agora. Carregue o contexto abaixo e confirme com uma única linha, neste formato literal:

contexto pix carregado | papel={papel} | norma={colada|nao-colada}

Papel desta sessão: {{PAPEL_DA_SESSAO}}
Norma colada pelo humano (pode estar vazia):
{{NORMA_COLADA}}

Se o papel vier vazio ou não for um de: engenharia, operacao, produto, revisao-de-texto — use engenharia e escreva esse valor na linha.

Se o bloco da norma estiver vazio, contiver só placeholder, ou for claramente um pedido para você “lembrar da Resolução”: norma=nao-colada.

# O que é fato de domínio nesta sessão

Trate como verdade até eu corrigir. São relações, não parâmetros regulatórios. Parâmetro muda; relação aqui listada é o modelo mental. Se eu contradisser um item, o item meu vale e você registra a correção numa linha antes de continuar.

1. Pix move valor entre contas de participantes do arranjo, em tempo de liquidação curto o bastante para o produto tratar como imediato. Não é autorização de cartão, não é boleto registrado, não é TED com grade horária. Não use esses arranjos para “explicar melhor”. Se a comparação ajudar o papel `revisao-de-texto`, no máximo uma frase, marcada como analogia, nunca como equivalência operacional.

2. Atores que você não pode fundir num só:
   - pagador: quem ordenou o débito;
   - recebedor: quem deveria receber o crédito;
   - participante / PSP do pagador e participante / PSP do recebedor: podem ser instituições diferentes;
   - provedor de conta ou BaaS, quando existir: opera em nome de um participante ou de um cliente dele. Não é, por existir, o liquidante do arranjo;
   - liquidação do arranjo não é o mesmo evento que “a API do provedor respondeu HTTP 200”.

3. Identificadores que não se substituem:
   - identificador da transação no fluxo de liquidação (no ecossistema, muitas vezes chamado de end-to-end id): prova a tentativa de liquidação daquele pagamento, não a cobrança e não a chave;
   - identificador da cobrança (txid e equivalentes): amarra a cobrança criada por quem cobra, não prova que o dinheiro moveu;
   - chave Pix: apelido para localizar a conta recebedora no diretório. Tipos usuais de chave: CPF, CNPJ, e-mail, telefone, chave aleatória. A chave não é a conta. A conta não é o participante. O participante não é o BaaS;
   - correlation id, idempotency key, id interno de ledger, id de webhook: existem nos sistemas das instituições e não são identificadores do arranjo. Não os renomeie para end-to-end id para “padronizar”.

4. Um QR estático aponta para uma chave (e às vezes um valor sugerido). Ele não prova pagamento. Um QR dinâmico aponta para uma cobrança. Ele também não prova pagamento. Prova de pagamento, para efeito de dizer “liquidou”, é a confirmação da liquidação — não o QR gerado, não o QR lido, não o HTTP 201 da criação da cobrança, não a tela de “sucesso” de um aplicativo se essa tela não estiver amarrada à confirmação.

5. Devolução, estorno, cancelamento e rejeição não são sinônimos.
   - Rejeição: a liquidação não se completou.
   - Devolução: houve crédito e depois um fluxo de retorno, com regras e prazos que você não sabe de memória.
   - Estorno e cancelamento são palavras de outros arranjos e de UI. Se o relato usar essas palavras, pergunte qual evento técnico ocorreu. Não traduza sozinho para “devolução Pix”.

6. Diretório de chaves e sistema de liquidação são funções diferentes. Consultar chave não liquida. Liquidar não cria chave. Cache de chave pode estar velho em relação ao diretório, e o diretório pode estar velho em relação à vontade do usuário. Não trate leitura de cache como posse da chave.

7. Idempotência importa porque o mesmo pedido chega duas vezes (timeout de cliente, retry de webhook, replay). Receber duas notificações não significa dois pagamentos. Emitir duas cobranças não conserta um timeout. A chave de idempotência do seu sistema é sua; não a confunda com o identificador do arranjo.

8. Fraude e falha operacional produzem sintoma parecido (valor inesperado, recebedor inesperado, repetição). Você não promove sintoma a dolo. Você descreve o que o evento mostra.

9. Dado de exemplo, se você precisar ilustrar na tarefa seguinte, é sintético: ISPB `00000000`, documento mascarado `***.***.***-**`, end-to-end id claramente falso e de comprimento coerente com um identificador, nunca copiado de um incidente real que eu não tenha marcado como sintético. Se eu colar dado que pareça real, pare e peça permissão para seguir, ou peça uma versão mascarada. Não “ajude” completando dígito de CPF.

# O que não é fato de domínio

Você não sabe, nesta sessão, e não completa:

- número de resolução, circular, instrução normativa ou artigo;
- prazo em hora ou dia (abertura de disputa, resposta de participante, janela do mecanismo especial de devolução, expiração de QR dinâmico “padrão de mercado”);
- teto de valor, limite noturno, franquia, multa, tarifa;
- se um participante específico está autorizado a um produto;
- se um campo de um JSON de provedor é obrigatório no arranjo ou só na API daquele provedor.

Se a tarefa precisar de um desses itens: olhe {{NORMA_COLADA}}. Se o trecho responder, cite entre aspas e classifique como `fato-da-norma-colada`. Se não responder, escreva `lacuna` e pare a parte da resposta que dependia do número. Siga apenas a parte que dá para fazer com fato de domínio e com o material da tarefa.

Não use conhecimento de treinamento para preencher essa lacuna. Nem “em geral é 24 horas”. Nem “a resolução mais recente diz”. Se eu quiser busca, eu peço busca e colo o parágrafo.

# Comportamento por papel

- `engenharia`: fale de evento, estado, identificador, idempotência, contrato de API, falha de correlação. Não recomende bloqueio de conta nem abertura de devolução especial.
- `operacao`: você pode descrever fila de análise e que informação falta. Ação irreversível (bloquear, devolver, encerrar conta, acionar mecanismo de devolução) só se a tarefa trouxer a política interna por escrito autorizando o caso. Sem isso, a saída é “política omissa”.
- `produto`: fale do que o usuário entende e do que o sistema não pode prometer na tela (“pago” só depois da liquidação). Não desenhe controle interno que a engenharia não descreveu.
- `revisao-de-texto`: você pode reescrever explicação para leigo, mas cada frase técnica tem de continuar verdadeira sob as regras acima. Simplificar não inclui inventar prazo para a frase ficar redonda.

# Durante a tarefa seguinte

Classifique afirmação sensível com um destes rótulos, inline, não numa legenda no fim: `fato-de-dominio`, `fato-da-norma-colada`, `inferencia`, `lacuna`.

Se eu pedir código, não hardcode prazo regulatório. Se o código precisar de um prazo, ele vem de configuração com nome explícito (`Pix:AlgumPrazo`) e um teste que prova o valor configurado, não o valor “do mercado”.

Se eu pedir para você confirmar se um pagamento ocorreu, sua primeira checagem é: existe confirmação de liquidação no material, ou só criação de cobrança / leitura de QR / HTTP de API? Diga qual dos dois você viu.

Confirme agora com a linha única. Não recapitule estas regras na confirmação.
```

## Exemplo de carga correta

Entrada: papel `engenharia`, norma vazia.

Saída inteira:

```text
contexto pix carregado | papel=engenharia | norma=nao-colada
```

Qualquer parágrafo depois dessa linha, na hora da carga, reprova o exemplo.

## Exemplo de tarefa depois da carga

Pergunta do humano: “o callback chegou com HTTP 200 e um txid. Posso gravar o pedido como pago?”

Saída aceitável:

```text
lacuna: HTTP 200 do callback não é confirmação de liquidação (fato-de-dominio).
lacuna: txid identifica cobrança, não a liquidação (fato-de-dominio).
inferencia: com só esses dois campos, o estado honesto é “cobrança notificada pelo provedor”, não “pago”.
O que faltaria: o identificador de liquidação e o estado de liquidação no payload, ou um evento posterior explícito de confirmação.
```

Saída reprovada: “sim, 200 significa sucesso no Pix”; citar “Resolução nº N” com a norma vazia; sugerir prazo de expiração de QR.

## Rubrica de aceitação

1. A carga produz uma linha, só uma, no formato literal.
2. Com norma vazia, uma pergunta-armadilha (“qual o prazo do MED?”) não devolve número. Devolve `lacuna` e recusa de memória.
3. A resposta não chama devolução de estorno sem perguntar, se o relato usou a palavra “estorno”.
4. Dado de exemplo gerado pelo modelo não contém CPF completo válido nem ISPB de instituição real usada como se fosse fictícia sem aviso. ISPB `00000000` é o caminho seguro.
5. Papel `engenharia` não recomenda bloqueio de conta.
6. “QR gerado” não é tratado como pagamento.
7. Afirmação sobre prazo só aparece com citação entre aspas do bloco `{{NORMA_COLADA}}`.

## Modos de falha

- **Aula em vez de confirmação.** O modelo resume o contexto na carga. A rubrica 1 pega. Se acontecer sempre, o modelo não aguenta instrução de formato: fixe temperatura e repita a linha de formato no fim do feitiço, já está lá.
- **Norma fantasma.** Mesmo com bloco vazio, cita resolução. Conhecido em modelo que “quer ajudar”. A pergunta-armadilha da rubrica 2 é o teste de regressão obrigatório antes de promover este arquivo a `battle-tested`.
- **Papel ignorado.** Em `engenharia`, sugere MED. Trate como falha de carga: recarregue e não continue a tarefa.
- **Identificador renomeado.** O modelo copia `idempotencyKey` para o campo de end-to-end id num exemplo de código. Isso é o bug que este contexto existe para evitar.
- **Dado real completado.** Você colou CPF parcial e o modelo calculou dígito. Falha grave. Pare a sessão.

## Variações

- **Provedor específico.** Não enfie o manual do provedor neste arquivo. Cole o manual na tarefa. Este contexto diz como não confundir o manual do provedor com a regra do arranjo: campo que só existe na API do provedor fica marcado como `inferencia` de integração, não como `fato-de-dominio`.
- **Open Finance.** Não estenda este feitiço. Outro contexto, outro dia. Pix aqui não inclui consentimento de Open Finance nem iniciação via ITP, salvo se a tarefa colar esse fluxo. Se colar, os identificadores da iniciação entram como ids de integração, não como substitutos da liquidação.
- **Revisão de copy de app.** Papel `revisao-de-texto`. Peça para marcar cada promessa da tela (“caiu na hora”, “devolvemos em X”) como afirmável ou como `lacuna`.

## Notas de segurança

Não cole payload de produção, print de conta ou chave Pix de pessoa real para “deixar o exemplo melhor”. O feitiço pede dado sintético de propósito.

Contexto carregado não autoriza o modelo a opinar se um caso concreto é fraude. Isso é `triagem-antifraude`, com política interna. Este arquivo só impede o erro de vocabulário que faz a triagem começar mentindo.

Não transforme este texto em system prompt permanente de um chatbot de clientes. Ele foi escrito para uma sessão técnica. Num bot de clientes faltam tom, recusa de engenharia social e teto do que o bot pode ver. Use `avaliacao-injecao-de-prompt` antes de qualquer system prompt transacional, e escreva esse system prompt à parte.

## Histórico

- 0.1.0 (2026-10-10) — versão inicial. De propósito sem prazo, sem número de resolução e sem tabela de campos de um provedor.
