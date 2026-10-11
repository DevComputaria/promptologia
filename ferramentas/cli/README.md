# CLI

O que existe hoje é o contrato, não um buscador.

```bash
python3 ferramentas/cli/check_grimorio.py
python3 ferramentas/cli/check_grimorio.py --write-catalog
```

O script falha se um feitiço estiver sem frontmatter, se o `id` repetir, se `battle-tested` não tiver saída em `exemplos/responses/<id>.md`, se um importado não tiver fonte, se um placeholder do corpo não estiver declarado, se algum nome de arquivo terminar em espaço, ou se `grimorio/CATALOGO.md` estiver velho.

Não há comando de busca. Índice é o catálogo gerado.
