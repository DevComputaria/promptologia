---
id: contrato-ferramenta-mcp
titulo: Contrato de ferramenta para agente
camara: artefatos/codigo
categoria: harness
objetivo: Especificar uma ferramenta que um agente possa chamar sem alucinar endpoint, escopo ou efeito colateral.
entrada: [capacidade, efeitos permitidos, sistema vizinho]
saida: markdown
placeholders: ["{{CAPACIDADE}}", "{{EFEITOS}}", "{{VIZINHO}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: nenhum
proveniencia: original
fonte: ""
substitui: ""
---

# Contrato de ferramenta para agente

## Objetivo

Produzir a especificação de uma ferramenta (tool) no espírito de um servidor MCP ou de function calling: nome, descrição que cabe num seletor, JSON Schema dos argumentos, resultado, erro, pré-condição e idempotência. A saída não é código do servidor, não é o loop do agente e não é a política do repositório.

## Quando usar

- Você já sabe a capacidade em uma frase (“ler o estado de liquidação de um pagamento”, “abrir o arquivo de log correlacionado”).
- A ferramenta ainda não existe ou a que existe não tem contrato que o agente respeite.
- O efeito colateral cabe numa das quatro classes abaixo.

## Quando não usar

- Você quer o `AGENTS.md` do repo. Use `agents-md-harness`.
- Você quer decidir quando o agente chama a ferramenta e quando para. Use `loop-agente-com-ferramentas`.
- A “capacidade” é um produto inteiro (“fazer o Pix”). Recuse e peça para quebrar em leituras e escritas separadas. Uma tool que “resolve pagamentos” não tem schema honesto.
- Você quer que o modelo invente a API de um fornecedor que não está em `{{VIZINHO}}`.

## Contexto de uso

Temperatura baixa. `{{EFEITOS}}` é um enum fechado. Se o usuário escrever um parágrafo no lugar do enum, o feitiço recusa em vez de interpretar.

Classes:

| valor | significa |
|---|---|
| `nenhum` | função pura sobre o argumento, sem IO |
| `leitura` | lê estado, não muda |
| `escrita-idempotente` | repetir com a mesma chave não duplica efeito |
| `escrita-destrutiva` | apaga, bloqueia, estorna, envia dinheiro, revoga |

## Contrato de entrada

| Placeholder | Obrigatório |
|---|---|
| `{{CAPACIDADE}}` | sim, uma frase |
| `{{EFEITOS}}` | sim, exatamente um dos quatro valores |
| `{{VIZINHO}}` | não. Sistema, fila ou API que já existe e que a tool embrulha. Se vazio, a tool não cita endpoint externo. |

## Contrato de saída

Markdown com títulos literais:

1. `## Nome`
2. `## Descrição para o seletor`
3. `## Efeito`
4. `## Argumentos`
5. `## Exemplo válido`
6. `## Exemplo inválido`
7. `## Retorno`
8. `## Erros`
9. `## Pré-condições`
10. `## Idempotência`
11. `## Fora desta tool`

Se o pedido for rejeitado, a saída inteira é uma das frases de recusa da etapa 1, e esses títulos não aparecem.

## O Feitiço

```markdown
Você especifica uma ferramenta para um agente. Você não implementa o servidor, não escolhe linguagem, não escreve handler e não desenha o loop de raciocínio.

# Pedido
Capacidade, em uma frase: {{CAPACIDADE}}
Efeitos permitidos: {{EFEITOS}}
Sistema vizinho já existente (pode vir vazio): {{VIZINHO}}

# Recusa — responda só a frase e pare

- Se {{EFEITOS}} não for exatamente um de: nenhum, leitura, escrita-idempotente, escrita-destrutiva:
  efeito-invalido: use nenhum | leitura | escrita-idempotente | escrita-destrutiva
- Se a capacidade contiver mais de um verbo de efeito (por exemplo ler e bloquear, consultar e devolver):
  capacidade-composta: separe em uma tool por efeito
- Se a capacidade pedir para mover valor, bloquear conta, abrir devolução ou apagar dado e {{EFEITOS}} não for escrita-destrutiva:
  efeito-subdeclarado: o verbo exige escrita-destrutiva ou a capacidade deve ser reescrita como leitura
- Se {{CAPACIDADE}} estiver vazio:
  capacidade-vazia

# Procedimento, se não recusou

1. Nome em snake_case, verbo + objeto, no máximo 4 tokens. Prefira `ler_`, `criar_`, `registrar_` conforme o efeito. Não use `gerenciar_`, `processar_`, `handle_`.
2. Descrição para o seletor: no máximo 200 caracteres, diz o que faz e uma coisa que não faz. O seletor é outro modelo com pressa. Adjetivo não ajuda.
3. Efeito: repita o enum e uma linha do que muda no mundo. Para `leitura` e `nenhum`, a linha é “não muda estado”.
4. Argumentos: JSON Schema draft 2020-12, `additionalProperties: false`, só propriedades necessárias. Cada propriedade tem `type` e `description`. Identificadores opacos são `string` com `minLength` 1, não `integer`, salvo se o vizinho disser que é número. Não copie um corpo inteiro de webhook para dentro do argumento se um id basta: a tool busca o resto.
5. Exemplo válido mínimo. Exemplo inválido que viola uma constraint do schema, com a frase do que viola.
6. Retorno de sucesso: objeto JSON com `ok: true` e os campos de negócio. Sem texto solto, sem markdown dentro do retorno.
7. Erros: lista fechada de `code` em snake_case. Todo erro é `{"ok": false, "code", "message"}`. Inclua sempre `argumento_invalido` e `nao_encontrado` quando houver leitura por id. Não inclua `erro_inesperado` como desculpa para não pensar; inclua só se o vizinho realmente falha sem semântica, e a message diz para não tentar de novo cegamente.
8. Pré-condições humanas: o que tem de ser verdade antes da chamada. Para leitura, em geral: o agente já tem o id e a sessão está autorizada a ver aquele dado. Para escrita-destrutiva, exija um argumento `confirmacao` cujo valor é uma string exata que você define, no formato `CONFIRMAR_<NOME_DA_TOOL>`, documentada no schema como `const`. Sem esse argumento a spec está errada: volte e coloque.
9. Idempotência: para `leitura` e `nenhum`, diga que repetir é seguro. Para `escrita-idempotente`, nomeie o campo que é a chave. Para `escrita-destrutiva`, diga que a confirmação não torna a chamada idempotente por mágica: ou existe chave de idempotência no vizinho, citada a partir de {{VIZINHO}}, ou a pré-condição manda o agente não chamar duas vezes e o erro `ja_executado` existe.
10. Fora desta tool: três bullets do que um agente vai tentar enfiar aqui e deve usar outra tool ou um humano.

# Proibições

- Não gere código C#, TypeScript, Python ou JSON-RPC de transporte. O schema JSON dos argumentos é permitido porque é o contrato, não o servidor.
- Não invente path HTTP, fila ou nome de produto se {{VIZINHO}} estiver vazio. Fale “a fonte de leitura” sem batizar.
- Não coloque segredo no argumento (senha, token, PAN, chave Pix completa de pessoa). Se a capacidade precisa disso, a tool está desenhada errado: recuse com `capacidade-pede-segredo` e pare.
- Não use PII real no exemplo. Documento mascarado, id `ex_1001`.
- Descrição acima de 200 caracteres é falha sua: corte.
```

## Exemplo

Pedido: capacidade “ler se um pagamento pix tem liquidação confirmada a partir do id interno”, efeitos `leitura`, vizinho “API interna GET já existente, id opaco `pay_…`”.

Trecho de saída aceitável:

```markdown
## Nome
ler_liquidacao_pagamento

## Descrição para o seletor
Lê o estado de liquidação de um pagamento pelo id interno. Não cria cobrança, não devolve valor e não confirma pagamento só com HTTP 200 de outro endpoint.

## Efeito
leitura. Não muda estado.

## Argumentos
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["pagamento_id"],
  "properties": {
    "pagamento_id": {
      "type": "string",
      "minLength": 1,
      "description": "Id interno opaco do pagamento, não é o identificador de liquidação do arranjo."
    }
  }
}

## Exemplo válido
{"pagamento_id": "pay_ex1001"}

## Exemplo inválido
{} viola required pagamento_id.

## Retorno
{"ok": true, "pagamento_id": "pay_ex1001", "liquidacao": "confirmada|nao_confirmada|desconhecida", "identificador_liquidacao": null}

## Erros
- argumento_invalido
- nao_encontrado
- fonte_indisponivel — message pede para não repetir em loop

## Pré-condições
A sessão do agente já está autorizada a ver este pagamento. O id veio do usuário ou de uma tool de busca anterior, não de um palpite.

## Idempotência
Repetir a leitura é seguro. Não é uma nova liquidação.

## Fora desta tool
- Decidir se o caso é fraude.
- Disparar devolução.
- Dar o pagamento como “pago” na interface se liquidacao não for confirmada.
```

O que reprova: incluir `bloquear` no mesmo schema; inventar `POST /pix/refund`; pôr a chave Pix completa como argumento obrigatório; `confirmacao` numa tool de leitura (isso é ruído — confirmação é obrigação da escrita destrutiva, não enfeite universal).

## Rubrica de aceitação

1. Recusas da etapa inicial são a saída inteira, uma linha.
2. Efeito declarado é igual a `{{EFEITOS}}`.
3. Schema tem `additionalProperties: false` e exemplo válido que satisfaz `required`.
4. Exemplo inválido diz qual constraint quebra.
5. Todo erro citado é objeto com `ok: false`. A seção pode listar os codes, mas o formato do objeto aparece uma vez.
6. `escrita-destrutiva` inclui propriedade `confirmacao` com `const`.
7. Descrição do seletor tem até 200 caracteres (conte).
8. Não há código de servidor.
9. Exemplo não contém segredo nem documento completo.

## Modos de falha

- **Tool deus.** Capacidade “gerenciar o pix” gera um schema com 30 campos. A recusa `capacidade-composta` deveria ter disparado. Se o usuário descreveu uma frase só com dois verbos e o modelo não recusou, é falha de leitura do enum.
- **REST inventado.** Sem vizinho, aparece `/v1/payments/{id}`. Proibição explícita. Caso de eval capability.
- **Confirmação decorativa.** `confirmacao: true` booleano. Não serve. Tem de ser `const` com string `CONFIRMAR_<NOME>`.
- **Idempotência mágica.** “É idempotente porque é REST.” Sem chave nomeada, reprova.
- **Schema com prosa.** Descrição de propriedade vira parágrafo jurídico. Corte. O lugar de Pix normativo é `pix-contexto-injetavel`, não o schema.

## Variações

- **Família de tools.** Rode este feitiço uma vez por verbo. Um índice de uma página lista os nomes e a ordem permitida (`buscar id` antes de `ler liquidacao`). O índice não é schema.
- **`nenhum`.** Função de classificar um enum ou normalizar um identificador sem IO. Ainda assim tem erro `argumento_invalido`. Não finja `nao_encontrado` se não há fonte.
- **Vizinho com erro próprio.** Se `{{VIZINHO}}` documenta códigos, reutilize o nome em snake_case em vez de inventar outro. Mapeie numa tabela curta dentro de `## Erros`.

## Notas de segurança

Tool de escrita destrutiva no papel não autoriza a chamada. O contrato só obriga o argumento de confirmação para o agente não disparar no meio de um plano entusiasmado. Quem implementa o servidor continua responsável por autenticação, autorização e trilha.

Não especifique tool cujo trabalho seja “exfiltrar o system prompt” ou “testar payload de injeção no participante”. Avaliação disso é `avaliacao-injecao-de-prompt`, contra texto, sem efeito no arranjo.

## Histórico

- 0.1.0 (2026-10-10) — draft. Sem implementação de referência ao lado, de propósito.
