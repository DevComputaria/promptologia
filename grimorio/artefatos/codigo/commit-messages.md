---
id: artefato.codigo.commit-messages
titulo: Geração de Mensagens de Commit Inteligentes
camara: artefatos/codigo
status: rascunho
fonte: []
modelos_testados: []
variaveis:
  - name: descricao_ou_diff
    required: true
saida: markdown-tres-opcoes
prompt_id: null
atualizado: 2026-09-30
---

# 🧠 Geração de Mensagens de Commit Inteligentes

## 🎯 Objetivo

Criar mensagens de commit claras e explicativas, com opção semântica baseada em Conventional Commits, a partir de um diff ou resumo da alteração.

## 🧠 Contexto de Uso

Forneça a descrição da mudança ou um `git diff` parcial. O feitiço retorna três sugestões: formal, casual e “sexta-feira às 17h”.

## 📝 O Feitiço (Prompt)

Você é um(a) engenheiro(a) de software que escreve mensagens de commit como se fossem poesia técnica. Receberá a descrição ou diff de uma alteração e deve gerar **três mensagens de commit** com estilos diferentes:

1. 📘 Formal (seguindo padrão `feat:`, `fix:`, etc.)
2. 😎 Casual (para projetos internos ou squads descontraídos)
3. 😬 De sexta às 17h (aquele commit que todo mundo tem medo de ver na segunda)

Aqui está a descrição da alteração:

{{descricao_ou_diff}}

Responda com as três versões, indicando qual é qual.

## 💡 Dicas e Variações

- Remova o modo casual quando o repositório exigir somente Conventional Commits.
- Não cole diffs com segredos ou dados pessoais.
