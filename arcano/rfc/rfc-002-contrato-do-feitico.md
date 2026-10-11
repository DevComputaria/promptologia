# RFC-002: O Contrato do Feitiço

**Status deste documento:** Normativo para arquivo novo. Retroativo para tudo que `ferramentas/cli/check_grimorio.py` já lê. O tom continua o da [RFC-001](rfc-001-diretrizes-caoticas.md). A regra, não.

**Data:** 2026-10-10

**Atualiza:** a seção 4 da RFC-001 ("Formatos de Prompt — Sugestões, Não Mandamentos"). Os princípios das seções 3 e 5 da RFC-001 continuam de pé. O que era sugestão de metadado passa a ser chave obrigatória.

**Autores (os mesmos culpados, mais um sem humor):**

*   A Comunidade DevComputaria
*   O checker, que não aceita piada no lugar de `id`

Se este texto e o checker discordarem, o checker ganha até este RFC ser emendado. Documento que descreve um programa e mente sobre o programa é fanfic.

## 1. Resumo

A RFC-001 disse que prompt é código e que um grimório de prompts testados em batalha vale mais do que originalidade às 3 da manhã. Não disse como o grimório recusa um feitiço sem dono, sem versão e sem saída conferível.

Este RFC fecha essa brecha. Um feitiço é um markdown com frontmatter completo, `id` único, proveniência honesta e placeholders que batem com o corpo. O catálogo é gerado. `battle-tested` sem arquivo de resposta é mentira, e o CI recusa a mentira.

O café da seção 6 da RFC-001 continua opcional. O frontmatter não.

## 2. O que deixa de ser sugestão

| RFC-001, seção 4 | RFC-002 |
|---|---|
| Título, categoria, objetivo, entrada e saída "que você deveria se importar" | Chaves obrigatórias. Arquivo sem elas não entra. |
| Placeholder `{{VARIAVEL_AQUI}}` como convenção | O conjunto declarado tem de ser exatamente o conjunto usado no corpo. |
| "Modelos de IA testados" como nota de rodapé | `modelos_testados` existe e começa vazio. Encher a lista não promove status. |
| Versionar `prompt_v3_agora_vai_confia.md` no nome do arquivo | `versao` no frontmatter. O nome do arquivo não carrega a versão. |
| Reutilizar sem vergonha | Reutilizar com `proveniencia: importado` e uma fonte. Empréstimo sem carimbo sai do disfarce de original. |
| Grimório como ideia | `grimorio/CATALOGO.md` gerado. Editar à mão é trabalho jogado fora no próximo `--write-catalog`. |

O sarcasmo da RFC-001 não é revogado. O que é revogado é a fachada: pasta anunciada e ausente, response de zero bytes, diretório com espaço no fim.

## 3. Escopo

O checker lê `*.md` em:

*   `grimorio/`
*   `ferramentas/integracoes/perplexity/`

Não lê:

*   `README.md` de câmara
*   `grimorio/CATALOGO.md`
*   `TEMPLATE.md` na raiz (é o molde; o `id` de exemplo mora lá de propósito)
*   qualquer caminho com `/examples/`
*   este RFC e o resto de `arcano/`

Nome de arquivo ou de diretório com espaço na ponta falha em qualquer lugar do repositório, inclusive fora do grimório. O Windows já mostrou o que faz com `PRD /`.

## 4. Frontmatter

O arquivo começa com `---`, uma chave por linha, e fecha com `---`. Linha sem `:` dentro do bloco é erro. Comentário com `#` é ignorado.

Chaves, nesta ordem, todas presentes:

```yaml
---
id: kebab-case-unico
titulo: Título humano
camara: artefatos/codigo
categoria: dev
objetivo: uma frase
entrada: ["o que o humano cola"]
saida: markdown
placeholders: ["{{NOME}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: nenhum
proveniencia: original
fonte: ""
substitui: ""
---
```

O checker exige a presença das dezesseis chaves. Não exige que `camara`, `categoria`, `entrada`, `saida` ou `versao` pertençam a um vocabulário fechado. Quem inventar `camara: almoxarifado` passa no CI e falha na leitura humana. O vocabulário que este RFC recomenda, sem o checker ainda aplicar, é:

| Chave | Valores recomendados |
|---|---|
| `camara` | `artefatos/codigo`, `artefatos/documentacao`, `artefatos/dados-e-scripts`, `artefatos/criativo`, `arquivos-de-contexto/sistema`, `arquivos-de-contexto/regras-de-negocio`, `arquivos-de-contexto/persona`, `tecnicas` |
| `categoria` | `dev`, `devops`, `secops`, `fintech`, `harness`, `humor`, `pesquisa` |
| `saida` | `markdown`, `json`, `texto` |
| `versao` | semver. Feitiço novo nasce `0.1.0`. |

`entrada` é lista curta do que o humano cola. Não é o prompt.

## 5. Identidade

`id` casa com `^[a-z0-9]+(-[a-z0-9]+)*$`. Único no conjunto que o checker lê. Repetir o `id` do `TEMPLATE.md` dentro de `grimorio/` é o jeito mais rápido de descobrir que o molde não é um feitiço e a cópia é.

`substitui` fica vazio, ou aponta o `id` do feitiço que este aposenta. O checker ainda não verifica se esse `id` existe. Apontar para um fantasma é dívida, não feature. Quando aposentar de verdade, o antigo vai para `status: superseded` e o novo declara `substitui`.

## 6. Status

Conjunto fechado: `draft`, `battle-tested`, `imported`, `superseded`.

| Status | Significado | O que o checker exige além da palavra |
|---|---|---|
| `draft` | Ninguém mediu a saída. | `proveniencia: original` |
| `battle-tested` | Existe saída real. | Arquivo `exemplos/responses/<id>.md` presente e com tamanho maior que zero |
| `imported` | O corpo veio de fora. | `proveniencia: importado` |
| `superseded` | Há sucessor. | Nada mecânico ainda. O sucessor deve preencher `substitui`. |

`draft` e `imported` não se misturam. `status: imported` com `proveniencia: original` falha. O inverso também.

Arquivo de resposta vazio não conta. Foi exatamente o defeito de `commit-messages-response.md` e `observabilidade-response.md`, removidos na fase 0. Inventar a saída para promover o status é fraude de medição. A fase 3 do plano continua fora: sem corrida real de modelo, não há feitiço `battle-tested` neste repositório, e o catálogo diz isso na cara.

`modelos_testados` só recebe modelo e data que alguém de fato rodou. Lista vazia é o estado honesto. Lista cheia sem o arquivo de resposta não muda o status.

## 7. Proveniência

`proveniencia` é `original` ou `importado`.

Importado precisa de `fonte` começando com `http://` ou `https://`, ou do literal `nao-identificada`. "Achei num gist que eu perdi" não é URL. `nao-identificada` é a confissão provisória, e o catálogo a mostra como `importado, fonte pendente`. Não é um estado para feitiço novo.

Não se reescreve o corpo de um importado para parecer da casa. Atribui-se a fonte, ou o arquivo sai. Isso já estava no `CONTRIBUTING.md`. Este RFC só torna a regra irmã do status.

`risco` é fechado: `nenhum`, `dados-sensiveis`, `uso-dual`.

*   `dados-sensiveis`: o feitiço pede log, transação, documento ou identificador que não deve vazar para o modelo errado. A RFC-001, seção 5, continua valendo: chave, segredo e fofoca da avó não entram no prompt.
*   `uso-dual`: o corpo do feitiço, não uma nota depois do bloco, declara o escopo autorizado. Avaliação de injeção descreve classe e critério. Não é kit contra terceiro. Pentest sem cerca no texto que o modelo lê continua defeito, e a fase 4 ainda não o corrigiu.

## 8. Placeholders

No corpo, placeholder é `{{NOME}}`. O checker extrai os nomes, tira a chave do que foi declarado em `placeholders`, ordena os dois conjuntos e compara.

Divergência falha. Declarar `{{CLIENTE}}` e usar `{{CLIENTE}}` mais um `{{ESQUECIDO}}` falha. Citar a forma do placeholder na prosa explicativa também conta como uso: se o texto didático precisa mostrar a marca, descreva com palavras ("a marca de placeholder"), não cole a marca.

Lista vazia é válida quando o corpo não tem nenhum.

## 9. Catálogo

`grimorio/CATALOGO.md` é saída de:

```bash
python3 ferramentas/cli/check_grimorio.py --write-catalog
```

Colunas: `id`, `status`, `risco`, proveniência, arquivo. Ordem alfabética de `id`. Quem editar a tabela à mão vê o CI reclamar que o arquivo está desatualizado.

O mesmo script, sem a flag, é o que roda no workflow `.github/workflows/grimorio.yml`. Falha com código 1. Não há modo leniente.

## 10. O que este RFC não faz

*   Não declara nenhum feitiço `battle-tested`. Não há response real.
*   Não aposenta o CRUD C#, o n8n partido, nem o pentest legado. Isso é a fase 4, uma PR por item.
*   Não reescreve o corpo dos imports para caber no template da casa. O carimbo chega. A cirurgia, não.
*   Não valida o vocabulário de `camara` e `categoria`. Recomenda. Apertar isso é emenda futura, quando o grimório parar de ganhar câmara nova toda semana.
*   Não substitui a RFC-001. Quem chegar aqui sem ter lido a primeira vai achar este texto seco. É de propósito. A piada mora lá. A trava mora aqui.

## 11. Café, de novo, só o necessário

A RFC-001 mede a cafeína pela complexidade do prompt. Este RFC acrescenta uma regra operacional: café não é evidência. "Rodei na minha cabeça e ficou bom" não preenche `exemplos/responses/`. O descafeinado continua julgado em silêncio.

---

**FIM DO RFC-002**

(Até o checker mudar, ou alguém marcar `battle-tested` sem o arquivo e descobrir o CI.)
