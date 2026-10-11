---
id: "copilot-instructions"
titulo: "Gerador de copilot-instructions"
camara: "arquivos-de-contexto/sistema"
categoria: "harness"
objetivo: "Prompt de terceiros que pede para gerar .github/copilot-instructions.md. Não é um AGENTS.md da casa. Corpo preservado."
entrada: ["repositório aberto no editor"]
saida: "markdown"
placeholders: []
modelos_testados: []
versao: "0.0.0"
status: "imported"
risco: "nenhum"
proveniencia: "importado"
fonte: "https://code.visualstudio.com/docs/copilot/customization/custom-instructions"
substitui: ""
---

> **Importado.** Corpo preservado, sem adaptação. Fonte: https://code.visualstudio.com/docs/copilot/customization/custom-instructions

Analyze this codebase to generate or update .github/copilot-instructions.md for guiding AI coding agents.

Focus on discovering the essential knowledge that would help an AI agents be immediately productive in this codebase. Consider aspects like:

The "big picture" architecture that requires reading multiple files to understand - major components, service boundaries, data flows, and the "why" behind structural decisions
Critical developer workflows (builds, tests, debugging) especially commands that aren't obvious from file inspection alone
Project-specific conventions and patterns that differ from common practices
Integration points, external dependencies, and cross-component communication patterns
Source existing AI conventions from **/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md} (do one glob search).

Guidelines (read more at https://aka.ms/vscode-instructions-docs):

If .github/copilot-instructions.md exists, merge intelligently - preserve valuable content while updating outdated sections
Write concise, actionable instructions (~20-50 lines) using markdown structure
Include specific examples from the codebase when describing patterns
Avoid generic advice ("write tests", "handle errors") - focus on THIS project's specific approaches
Document only discoverable patterns, not aspirational practices
Reference key files/directories that exemplify important patterns
Update .github/copilot-instructions.md for the user, then ask for feedback on any unclear or incomplete sections to iterate.
