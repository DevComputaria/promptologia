# RFC-002: Registro e Versionamento do Grimório

**Status:** Aceito

**Data:** 2026-09-30

## Resumo

Feitiços precisam de identidade estável sem depender do nome engraçado que receberam na sexta-feira. Este RFC define o registro mínimo do grimório e separa sua evolução editorial do versionamento de contratos executáveis.

## Identidade e estado

Cada feitiço registrado declara no frontmatter:

- `id`, estável e independente do caminho;
- `status`: `rascunho`, `testado`, `ponte` ou `arquivado`;
- `atualizado`, em `AAAA-MM-DD`;
- `modelos_testados`, mesmo quando a lista estiver vazia;
- `prompt_id`, nulo até existir uma promoção real.

O histórico vive no Git. Nomes como `_final`, `_final_mesmo` e `_agora_vai_confia` continuam permitidos em piadas de commit, não na identidade de um feitiço.

## Progressão

1. `rascunho`: estrutura revisável, ainda sem evidência de execução.
2. `testado`: possui ao menos uma execução identificada por modelo e um exemplo reproduzível.
3. `ponte`: aponta para um contrato imutável e versionado no repositório `DevComputaria.Prompting`.
4. `arquivado`: mantido para histórico, mas não recomendado para novos usos.

Alterar o status ou a data não cria outra identidade. Mudanças ficam no histórico do arquivo e devem explicar o efeito sobre variáveis e saída.

## Fronteira do contrato

Markdown neste repositório é material humano: ficha, feitiço, skill, exemplo e ponte. Quando houver consumidor, variáveis estáveis e saída observável, o contrato nasce em `DevComputaria.Prompting` sob `prompts/{domain}/{slug}/{semver}.yaml`. Uma versão publicada não é editada; publica-se outra versão e atualiza-se a ponte aqui.

## Consequências

- `grimorio/INDEX.md` passa a ser o cartório navegável.
- `scripts/index-grimorio.py` deriva o índice do frontmatter.
- Migrações podem ocorrer por câmara; arquivos ainda não registrados aparecem explicitamente como legado.
- Sufixo teatral não substitui status, data nem histórico.
