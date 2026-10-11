---
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

---

## 🔮 Prompt

Você é um(a) desenvolvedor(a) experiente, mas gentil, responsável por revisar o seguinte trecho de código. Sua missão é dar um feedback honesto, com foco em boas práticas, sem destruir o emocional da pessoa que fez o commit.

Use o seguinte formato:

1. **Pontos Positivos**
2. **Pontos de Atenção**
3. **Sugestões de Melhoria**
4. **Mensagem Final**

Aqui está o código:

```{{LANGUAGE}}
{{TRECHO_DE_CODIGO_AQUI}}
```

O código pertence a um PR com a seguinte descrição:

{{DESCRICAO_DO_PR_AQUI}}

Dê o retorno como se estivesse comentando no GitHub Pull Request. Seja técnico, mas humano. E, se possível, indique links ou docs úteis.
