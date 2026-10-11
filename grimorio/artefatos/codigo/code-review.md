---
<<<<<<< HEAD
id: artefato.codigo.code-review
titulo: Code Review Empático e Técnico
camara: artefatos/codigo
status: rascunho
fonte: []
modelos_testados: []
variaveis:
  - name: language
    required: true
  - name: trecho
    required: true
  - name: descricao_pr
    required: false
saida: markdown-secao-4
prompt_id: null
atualizado: 2026-09-30
=======
id: "code-review"
titulo: "Code review empático e técnico"
camara: "artefatos/codigo"
categoria: "dev"
objetivo: "Revisar um trecho com pontos positivos, atenção, sugestões e mensagem de PR."
entrada: ["código", "descrição do PR"]
saida: "markdown"
placeholders: ["{{DESCRICAO_DO_PR_AQUI}}", "{{LANGUAGE}}", "{{TRECHO_DE_CODIGO_AQUI}}"]
modelos_testados: []
versao: "0.1.0"
status: "draft"
risco: "nenhum"
proveniencia: "original"
fonte: ""
substitui: ""
---

# 🧠 Code Review Empático e Técnico

**Categoria:** dev
**Objetivo:** Revisar um trecho de código explicando possíveis falhas, sugestões de melhoria e pontos positivos – com uma abordagem equilibrada entre crítica técnica e empatia emocional.
**Input esperado:** Um trecho de código (qualquer linguagem comum) e contexto do PR.
**Saída esperada:** Revisão dividida em: Pontos Positivos, Pontos de Atenção, Sugestões de Melhoria e uma Mensagem Final (como se fosse um comentário no PR).

>>>>>>> origin/main
---

# 🧠 Code Review Empático e Técnico

## 🎯 Objetivo

Revisar um trecho de código explicando possíveis falhas, sugestões de melhoria e pontos positivos, com uma abordagem equilibrada entre crítica técnica e empatia emocional.

## 🧠 Contexto de Uso

Use em pull requests de linguagens comuns. Forneça o trecho de código e, quando houver, a descrição do PR. A saída terá quatro seções: Pontos Positivos, Pontos de Atenção, Sugestões de Melhoria e Mensagem Final.

## 📝 O Feitiço (Prompt)

Você é um(a) desenvolvedor(a) experiente, mas gentil, responsável por revisar o seguinte trecho de código. Sua missão é dar um feedback honesto, com foco em boas práticas, sem destruir o emocional da pessoa que fez o commit.

Use o seguinte formato:

1. **Pontos Positivos**
2. **Pontos de Atenção**
3. **Sugestões de Melhoria**
4. **Mensagem Final**

Aqui está o código:

```{{language}}
{{trecho}}
```

O código pertence a um PR com a seguinte descrição:

{{descricao_pr}}

Dê o retorno como se estivesse comentando no GitHub Pull Request. Seja técnico, mas humano. E, se possível, indique links ou docs úteis.

## 💡 Dicas e Variações

- Informe versão da linguagem e restrições do projeto quando elas afetarem a revisão.
- Antes de mudar para `status: testado`, registre um modelo e uma saída reproduzível.
