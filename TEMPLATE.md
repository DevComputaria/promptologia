---
id: exemplo-nao-copiar-este-arquivo
titulo: Título claro
camara: artefatos/codigo
categoria: dev
objetivo: Uma frase. O que o feitiço devolve e o que ele recusa.
entrada: ["o que o humano cola"]
saida: markdown
placeholders: ["{{EXEMPLO}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: nenhum
proveniencia: original
fonte: ""
substitui: ""
prompt_id: null
---

# Nome do Feitiço

Este arquivo é o modelo. Ele fica na raiz e o checker não o lê. Ao copiar para `grimorio/`, troque o `id`. Se o `id` continuar `exemplo-nao-copiar-este-arquivo`, o checker acusa repetição assim que existir um segundo.

## Objetivo

Uma frase.

## Quando usar

O caso em que o feitiço é a ferramenta certa.

## Quando não usar

O caso vizinho que parece o mesmo e não é. Sem esta seção o feitiço vaza para a tarefa errada.

## O Feitiço

```markdown
Texto que a pessoa cola. Placeholder no formato {{EXEMPLO}}, maiúsculas, e o mesmo nome declarado no frontmatter.
Se a entrada obrigatória vier vazia, responda com uma linha de recusa e pare.
```

## Exemplo

Entrada mínima sintética e a saída que conta como acerto. Dado real de cliente não entra.

## Rubrica de aceitação

Condições mecânicas. "Ficou bom" não é condição.

## Modos de falha

Como este tipo de pedido costuma quebrar, e o que fazer com a saída quando quebrar.

## Histórico

- 0.1.0 — rascunho, sem modelo testado.

`status` só vira `battle-tested` com arquivo não vazio em `exemplos/responses/<id>.md`.
`risco: uso-dual` exige escopo autorizado no corpo do feitiço, não numa nota depois do bloco.

`prompt_id` só é preenchido após a promoção para uma versão fixa em `DevComputaria.Prompting`.
