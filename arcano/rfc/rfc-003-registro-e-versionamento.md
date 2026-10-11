# RFC-003: Registro e Versionamento do Grimório

**Status:** Aceito

**Data:** 2026-10-11

**Complementa:** [RFC-002: O Contrato do Feitiço](./rfc-002-contrato-do-feitico.md)

## Resumo

Feitiços precisam de identidade estável sem depender do nome engraçado que receberam na sexta-feira. A RFC-002 define o frontmatter e os status válidos; este documento esclarece como a identidade local se relaciona com contratos executáveis publicados em `DevComputaria.Prompting`.

## Identidade e histórico

Cada feitiço segue o frontmatter normativo da RFC-002. Seu `id` permanece estável e independente do caminho; alterações editoriais ficam no histórico do Git. Nomes como `_final`, `_final_mesmo` e `_agora_vai_confia` continuam permitidos em piadas de commit, não na identidade de um feitiço.

`modelos_testados` só contém modelos realmente executados. Uma lista preenchida não substitui a evidência exigida pela RFC-002 para `battle-tested`.

## Fronteira do contrato

Markdown neste repositório é material humano: ficha, feitiço, skill, exemplo e ponte. Quando houver consumidor, variáveis estáveis e saída observável, o contrato nasce em `DevComputaria.Prompting` sob `prompts/{domain}/{slug}/{semver}.yaml`. Uma versão publicada não é editada; publica-se outra versão e atualiza-se a ponte aqui.

`prompt_id` permanece nulo até existir uma promoção real para uma versão fixa. Não use aliases como `latest`, copie a árvore `prompts/` para este repositório nem edite aqui uma versão já publicada.

O status continua seguindo a RFC-002: `draft`, `battle-tested`, `imported` ou `superseded`. A mudança de status, por si só, não altera a identidade nem publica um contrato.

## Consequências

- `grimorio/INDEX.md` deriva do frontmatter por meio de `scripts/index-grimorio.py`.
- O catálogo contratual `grimorio/CATALOGO.md` é gerado pelo checker da RFC-002.
- Sufixo teatral não substitui identidade, versão nem histórico.
