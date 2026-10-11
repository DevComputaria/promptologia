---
id: "commit-messages"
titulo: "Mensagens de commit"
camara: "artefatos/codigo"
categoria: "dev"
objetivo: "Gerar três mensagens de commit a partir de um diff ou descrição."
entrada: ["diff ou descrição"]
saida: "markdown"
placeholders: ["{{DESCRICAO_OU_DIFF_AQUI}}"]
modelos_testados: []
versao: "0.1.0"
status: "draft"
risco: "nenhum"
proveniencia: "original"
fonte: ""
substitui: ""
---

# 🧠 Geração de Mensagens de Commit Inteligentes

**Categoria:** dev
**Objetivo:** Criar mensagens de commit claras, explicativas e com padrão semântico (ex: Conventional Commits), a partir de um diff ou resumo da alteração.
**Input esperado:** Descrição da alteração ou `git diff` parcial.
**Saída esperada:** 3 sugestões de mensagens de commit – uma formal, uma casual e uma "commit de sexta-feira às 17h".

---

## 🔮 Prompt

Você é um(a) engenheiro(a) de software que escreve mensagens de commit como se fossem poesia técnica. Receberá a descrição ou diff de uma alteração e deve gerar **três mensagens de commit** com estilos diferentes:

1. 📘 Formal (seguindo padrão `feat:`, `fix:`, etc.)
2. 😎 Casual (para projetos internos ou squads descontraídos)
3. 😬 De sexta às 17h (aquele commit que todo mundo tem medo de ver na segunda)

Aqui está a descrição da alteração:

{{DESCRICAO_OU_DIFF_AQUI}}

Responda com as três versões, indicando qual é qual.
