---
id: "observabilidade-incident-template"
titulo: "Template de incidente de observabilidade"
camara: "tecnicas"
categoria: "devops"
objetivo: "Duplicata de observabilidade.md. A fase 4 troca este corpo por um ponteiro; não foi apagada nesta PR."
entrada: ["stacktrace ou relato"]
saida: "markdown"
placeholders: ["{{DESCRICAO_OU_STACKTRACE}}"]
modelos_testados: []
versao: "0.1.0"
status: "draft"
risco: "nenhum"
proveniencia: "original"
fonte: ""
substitui: ""
---

```markdown
# 🧠 Investigação de Incidente de Observabilidade

**Categoria:** devops
**Objetivo:** Auxiliar na análise de falhas em serviços Kubernetes gerando sugestões de métricas, logs e traces a partir de um stacktrace ou descrição.
**Input esperado:** Stacktrace ou relato do incidente com detalhes do serviço.
**Saída esperada:** Lista de coletas recomendadas, queries de exemplo e possíveis melhorias de monitoramento.

---

## 🔮 Prompt

Você é um engenheiro de observabilidade experiente. Analise o incidente abaixo e produza:
1. Resumo do problema.
2. Métricas e logs a coletar.
3. Exemplos de consultas de trace (OpenTelemetry).
4. Painéis ou alertas que podem ser criados para prevenção.

**Incidente:** `{{DESCRICAO_OU_STACKTRACE}}`

Responda em Markdown organizado em seções.

---

## 💡 Notas
- Personalize as ferramentas citadas (Prometheus, Grafana, etc.) conforme o ambiente.
- Útil para times de SRE e DevOps.
```
