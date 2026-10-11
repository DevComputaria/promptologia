---
id: "base-prompt-template"
titulo: "Template base de prompt"
camara: "tecnicas"
categoria: "harness"
objetivo: "Modelo genérico de seção para um feitiço novo. O exemplo interno é de observabilidade."
entrada: ["stacktrace de exemplo"]
saida: "markdown"
placeholders: ["{{STACKTRACE_HERE}}"]
modelos_testados: []
versao: "0.1.0"
status: "draft"
risco: "nenhum"
proveniencia: "original"
fonte: ""
substitui: ""
---

```markdown
# 🧠 Título do Prompt

**Categoria:** dev / devops / secops / humor / outro
**Objetivo:** O que esse prompt resolve? (ex: gerar um diagrama de threat modeling a partir de logs)
**Input esperado:** (ex: código, stacktrace, texto livre)
**Saída esperada:** (ex: resposta técnica, explicação passo a passo)

---

## 🔮 Prompt

Você é um engenheiro de observabilidade que trabalha em sistemas distribuídos no Kubernetes. Sua função é analisar o seguinte stacktrace e sugerir pontos de métrica, log e trace.

Stacktrace: {{STACKTRACE_HERE}}

Responda em formato Markdown, com código de exemplo e recomendações.

---

## 💡 Notas

- Pode ser adaptado para logs de outras linguagens.
- Ideal para uso com GPT-4 ou Claude.
- Testado com observabilidade de APIs REST.
```
