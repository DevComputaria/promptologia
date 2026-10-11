# Como contribuir

1. Forka com responsabilidade (ou desespero).
2. Crie seu feitiço a partir do [`TEMPLATE.md`](./TEMPLATE.md). Para estruturas especializadas, consulte os modelos em [`grimorio/tecnicas/templates/`](./grimorio/tecnicas/templates/).
3. Gere e valide o índice com `python3 scripts/index-grimorio.py` e `python3 scripts/index-grimorio.py --check`.
4. Rode `python3 ferramentas/cli/check_grimorio.py` antes do push; o CI roda o mesmo contrato.
5. Não marque `battle-tested` sem `exemplos/responses/<id>.md` com conteúdo, data e modelo.
6. Não reescreva o corpo de arquivo `proveniencia: importado`. Atribua a fonte ou retire o arquivo.
7. O backlog está em [PLANO-DE-MUDANCAS.md](PLANO-DE-MUDANCAS.md). Eval com saída inventada não conta. Aposentadoria de CRUD, n8n e pentest é uma PR por item.
8. Abra uma PR com título sarcástico mas explicativo; responda aos comentários com sabedoria ou memes.
