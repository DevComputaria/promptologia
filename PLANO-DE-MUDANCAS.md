# Plano de mudanças — promptologia

**Status:** fases 0, 1 e 2 estão nesta branch (`feat/contrato-do-grimorio`). Fase 3 não entra: exigiria saída real de modelo, e inventar `exemplos/responses/` seria fraude de medição. Fase 4 continua uma PR por item (CRUD C# moderno, ponte da duplicata de observabilidade, cerca do pentest dentro do corpo, n8n partido em dois).
**Data:** 2026-10-10
**Não é:** reescrita estética do tom DevComputaria. O sarcasmo do RFC-001 fica. O que sai é fachada, duplicata e prompt sem contrato.

Este documento é o backlog. Cada fase cabe numa PR. Não misture higiene de path com feitiço novo na mesma revisão: o diff fica ilegível e o que quebra no Windows (espaço no fim do diretório) se esconde no meio de markdown.

## 1. Diagnóstico que justifica o plano

O repositório tem três linhagens que não compartilham contrato.

| Linhagem | Onde | Problema |
|---|---|---|
| Casa | `grimorio/artefatos/codigo/*`, observabilidade, threat model, pentest | Curtos, usáveis, sem versão, sem saída de referência |
| Importado | toolkit PRD/MVP, Perplexity, MARM, Ailoen, `copilot-instructions.md` | Sem proveniência, sem o template, um deles cita arquivo que não existe (`HANDBOOK.md`) |
| Fachada | pastas citadas nos READMEs e ausentes no disco | `documentacao/`, `regras-de-negocio/`, `arcano/estudos/`, `contextos/projetos/`, `contextos/tecnologias/`, `ferramentas/cli/` |

Fatos medidos em 2026-10-10, clone raso de `main`:

- 66 arquivos, ~2.600 linhas.
- `exemplos/responses/commit-messages-response.md` e `observabilidade-response.md` têm 0 bytes.
- Sete diretórios do AI Product Development Toolkit terminam com espaço (`PRD /`, `MVP /`, …).
- `observabilidade.md` e `observabilidade-incident-template.md` são o mesmo feitiço.
- `CONTRIBUTING.md` aponta para `templates/` na raiz. O path real é `grimorio/tecnicas/templates/`.
- A câmara de técnicas anuncia few-shot, chain-of-thought e autocrítica como “em breve”.

Conclusão registrada antes da branch: adicionar prompt sem schema piorava a descoberta. A branch executa as fases 0 a 2. O espaço no fim dos diretórios do toolkit e o arquivo Perplexity com espaço no nome foram renomeados. Os dois responses de zero bytes foram removidos.

## 2. Princípios

1. Prompt é artefato versionável. Todo feitiço novo nasce com frontmatter. Feitiço velho ganha frontmatter na fase 1, sem reescrever o corpo.
2. Uma câmara, um trabalho. Contexto não pede tarefa. Artefato não redefine persona global. Técnica ensina o método em cima de um feitiço que já existe.
3. Número de norma, prazo regulatório e limite de valor não entram no grimório de memória. O feitiço exige o trecho da fonte primária. Inventar artigo da Resolução BCB é defeito, não completude.
4. Segurança ofensiva fica atrás de escopo autorizado no corpo do prompt, não numa nota que o modelo não vê. Avaliação de injeção descreve classe e critério de aprovação. Não é kit de ataque contra terceiro.
5. Sem exemplo conferível, o status permanece `draft`. “Battle-tested” é mentira até existir uma saída real em `exemplos/responses/`.
6. Importado não se disfarça de original. `proveniencia: importado` mais URL, ou sai do índice principal.

## 3. Estado alvo da árvore

```text
promptologia/
  PLANO-DE-MUDANCAS.md          # este arquivo
  TEMPLATE.md                   # passa a exigir o frontmatter (fase 1)
  CATALOGO.md                   # gerado; semente manual já em grimorio/CATALOGO.md
  grimorio/
    artefatos/
      codigo/                   # existentes + contrato-ferramenta-mcp.md
      documentacao/             # NOVA: postmortem-sem-culpa.md
      dados-e-scripts/          # existente + triagem-antifraude.md
    arquivos-de-contexto/
      regras-de-negocio/        # NOVA: pix-contexto-injetavel.md
      sistema/
        agents-md-harness.md
        secops/                 # NOVA, separada de secops-legacy
          avaliacao-injecao-de-prompt.md
    tecnicas/
      few-shot-cot-autocritica.md
      eval-control-edge-capability.md
      loop-agente-com-ferramentas.md
```

`secops-legacy/` permanece até a fase 4 decidir o que fundir. Não se move arquivo velho no mesmo commit que cria arquivo novo.

## 4. Contrato de frontmatter

Obrigatório em todo markdown que contenha um feitiço. READMEs de câmara ficam de fora.

```yaml
---
id: kebab-case-unico
titulo: Título humano
camara: artefatos/codigo | artefatos/documentacao | artefatos/dados-e-scripts | arquivos-de-contexto/sistema | arquivos-de-contexto/regras-de-negocio | tecnicas
categoria: dev | devops | secops | fintech | harness | humor | pesquisa
objetivo: uma frase
entrada: [lista curta]
saida: markdown | json | texto
placeholders: ["{{NOME}}"]
modelos_testados: []          # preencher só com modelo e data reais
versao: 0.1.0
status: draft | battle-tested | imported | superseded
risco: nenhum | dados-sensiveis | uso-dual
proveniencia: original | importado
fonte: ""                     # URL se importado
substitui: ""                 # id de outro feitiço, se for o caso
---
```

Regras do checker (fase 1, script único, sem framework):

- `id` único no repositório.
- `status: battle-tested` exige arquivo não vazio em `exemplos/responses/<id>.md`.
- `proveniencia: importado` exige `fonte` com `http`.
- Diretório e nome de arquivo não podem terminar em espaço, nem conter ` -` acidental.
- Placeholder no corpo usa `{{MAIUSCULAS_COM_UNDERSCORE}}`. Colchete `[Tipo de Documento]` não conta.

Até o checker existir, revisão humana na PR usa esta lista.

## 5. Fases

### Fase 0 — Higiene de path e índice mentiroso

Feito nesta branch: diretórios do toolkit sem espaço final, Perplexity renomeado, responses de zero bytes removidos, CONTRIBUTING apontando para o template certo, proveniência no topo dos importados, pastas que eram link morto com README curto (`arcano/estudos/`, `contextos/projetos/`, `contextos/tecnologias/`, `ferramentas/cli/`).

| Ação | Alvo |
|---|---|
| Renomear diretórios com espaço final | `grimorio/tecnicas/templates-para-projetos/ai-product-development-toolkit/*/` |
| Renomear arquivo | `ferramentas/integracoes/perplexity/Resumo -e-Antecedentes-da-Empresa-e-Due-Diligence.md` → `resumo-antecedentes-due-diligence.md` |
| Apagar ou preencher | `exemplos/responses/*.md` com 0 bytes. Vazio não fica. |
| Corrigir | `CONTRIBUTING.md` aponta para `grimorio/tecnicas/templates/` e para este plano |
| Carimbar proveniência no topo, sem reescrever o corpo | toolkit, MARM, Ailoen, `copilot-instructions.md`, prompts Perplexity |
| Decidir link morto | `arcano/estudos/`, `contextos/projetos/`, `contextos/tecnologias/`, `ferramentas/cli/`: ou um README de 10 linhas dizendo “não há conteúdo”, ou o link sai do índice pai |

Critério de aceite: `find` não acha nome terminado em espaço; nenhum link relativo do `README.md` raiz ou dos READMEs de câmara aponta para path inexistente; `git status` dessa PR não contém os feitiços da fase 2.

### Fase 1 — Contrato

Feito nesta branch: `TEMPLATE.md`, frontmatter nos feitiços que já existiam (corpo preservado), `ferramentas/cli/check_grimorio.py`, catálogo gerado e workflow `.github/workflows/grimorio.yml`.

- Atualizar `TEMPLATE.md` para o frontmatter desta seção 4 mais as seções já usadas pela casa (Objetivo, Quando não usar, Feitiço, Exemplo, Rubrica, Modos de falha).
- Frontmatter nos feitiços antigos da casa, corpo intocado: code-review, commit-messages, os três de C#, observabilidade, workflow-n8n, threat-modeling, pentest, cicd-security-assessment.
- `CATALOGO.md` na raiz, gerado por script que lê o YAML. A semente manual está em [grimorio/CATALOGO.md](grimorio/CATALOGO.md) e deve ser substituída pelo gerado, não mantida em paralelo.
- CI mínima: o script retorna código ≠ 0 se o contrato quebrar. GitHub Actions cabe em um job de `python`. Sem Node obrigatório.

Critério de aceite: os oito feitiços da casa acima têm frontmatter válido; o script roda limpo em cima deles e dos feitiços novos.

### Fase 2 — Feitiços novos (esta entrega)

Feito nesta branch. Todos `status: draft`, `versao: 0.1.0`, `proveniencia: original`. Nenhum se declara battle-tested.

| id | Arquivo | Por que existe |
|---|---|---|
| `agents-md-harness` | `grimorio/arquivos-de-contexto/sistema/agents-md-harness.md` | O `copilot-instructions.md` atual é prompt de terceiros para um artefato curto. Harness de 2026 lê `AGENTS.md` com proibição e comando de verificação. |
| `pix-contexto-injetavel` | `grimorio/arquivos-de-contexto/regras-de-negocio/pix-contexto-injetavel.md` | A câmara `regras-de-negocio/` estava no índice e não existia. Contexto, não tarefa. Não embute artigo nem prazo. |
| `triagem-antifraude` | `grimorio/artefatos/dados-e-scripts/triagem-antifraude.md` | Threat model STRIDE não opera alerta. Este opera, sem ação irreversível por conta própria. |
| `eval-control-edge-capability` | `grimorio/tecnicas/eval-control-edge-capability.md` | Fecha o ciclo que o RFC-001 descreve e o repo não pratica: o feitiço se testa. |
| `contrato-ferramenta-mcp` | `grimorio/artefatos/codigo/contrato-ferramenta-mcp.md` | Agente sem contrato de ferramenta alucina endpoint. A saída é spec, não servidor. |
| `avaliacao-injecao-de-prompt` | `grimorio/arquivos-de-contexto/sistema/secops/avaliacao-injecao-de-prompt.md` | Rubrica defensiva. Classe e critério. Sem payload contra instituição real. `risco: uso-dual`. |
| `few-shot-cot-autocritica` | `grimorio/tecnicas/few-shot-cot-autocritica.md` | Tira o “em breve” da câmara de técnicas usando o feitiço de commit como espécime. |
| `loop-agente-com-ferramentas` | `grimorio/tecnicas/loop-agente-com-ferramentas.md` | O loop planificar → ferramenta → observar → parar. Complementa o contrato MCP; não o repete. |
| `postmortem-sem-culpa` | `grimorio/artefatos/documentacao/postmortem-sem-culpa.md` | Enche `documentacao/`, que era link morto, e conversa com o feitiço de observabilidade já existente. |

Fora desta fase, de propósito:

- Não reescrever os três geradores C# de CRUD/DTO/teste de controller. Estão datados (.NET 6, controller clássico, piada de Stroustrup). Reescrever é fase 4, um feitiço que substitui, não um quarto CRUD ao lado.
- Não converter os 10 prompts Perplexity para o template agora. São atalhos de pesquisa. Fase 4 marca ou move.
- Não “melhorar” o workflow n8n no mesmo PR. Ele atribui ao modelo capacidade de runtime (validar endpoint, detectar loop). Quebrar em dois feitiços é fase 4.

Critério de aceite da fase 2: os nove arquivos existem; cada um tem as seções Objetivo, Quando não usar, Feitiço, pelo menos um exemplo completo, rubrica mecânica e modos de falha; placeholders do corpo estão declarados no frontmatter.

### Fase 3 — Eval de verdade

Rodar `eval-control-edge-capability` em cima de, nesta ordem:

1. `commit-messages.md` (curto, fácil de julgar).
2. `code-review.md`.
3. `threat-modeling.md`.
4. `triagem-antifraude` (o novo, para não passar o próprio feitiço de eval sem ser medido).

Cada rodada produz `exemplos/responses/<id>.md` com data, modelo e o veredito. Só então o feitiço pode ir a `battle-tested`. Caso esperado de quebra nos antigos: placeholder `{{...}}` chegando literal, porque o corpo não diz o que fazer.

Critério de aceite: quatro arquivos de response não vazios; pelo menos um achado vira mudança de versão `0.1.0` → `0.2.0` no feitiço alvo, com o id do caso citado.

### Fase 4 — Aposentadoria e substituição

Uma PR por item. `substitui:` preenchido, o antigo fica `status: superseded` por uma release antes de sumir.

| Item | Destino |
|---|---|
| Duplicata de observabilidade | Manter `observabilidade.md`. O template vira ponte de 5 linhas apontando para ele, ou sai. |
| CRUD / DTO DataAnnotations / teste de controller | Um feitiço `csharp-api-moderna` (Minimal API ou controller, `ProblemDetails`, validação, `CancellationToken`, teste do comportamento HTTP). Não três boilerplate. |
| `pentest-generation.md` | Fundir a cerca de escopo autorizado que está em `avaliacao-injecao-de-prompt` para dentro do corpo. Sem isso o modelo não vê a restrição. |
| Workflow n8n | Dividir: desenho conversacional e emissão de JSON só com tipos de nó que o autor listar no input. |
| Perplexity | Pasta continua, status `imported`, fora do catálogo de feitiços até alguém reescrever um de cada vez. |
| Ailoen e MARM | Permanecem como referência importada ou saem. Não entram no caminho feliz do catálogo. |

## 6. Ordem de PR sugerida

1. `chore: tira espaço do path e link morto` — fase 0.
2. `docs: contrato de frontmatter e catalogo` — fase 1.
3. `feat: feitiços de harness, pix, fraude, eval e incidente` — fase 2, os nove arquivos mais os READMEs de câmara. Este working tree já é essa PR, mais o plano. Na hora de abrir, não incluir renomeação da fase 0.
4. `test: primeiras quatro evals` — fase 3, assim que alguém rodar de fato contra um modelo. Não inventar a saída.
5. Fase 4, PRs pequenas, depois.

## 7. Riscos

| Risco | Mitigação no plano |
|---|---|
| Grimório virar manual jurídico desatualizado de Pix/BCB | Contexto Pix recusa prazo e artigo de memória |
| Feitiço de fraude sugerir bloqueio ou MED sem política | Saída obrigatória “política omissa — não recomendo ação irreversível” |
| Avaliação de injeção ser lida como exploit | Sem alvo real, sem passo de fraude, `risco: uso-dual`, recusa se o escopo vier vazio |
| Import sem licença | Fase 0 carimba fonte; se a licença do toolkit não for compatível com a licença da casa, o diretório sai em vez de ser reformatado |
| Volume | Nove feitiços longos é o teto desta leva. O próximo prompt novo precisa apontar qual câmara vazia ele fecha |

## 8. Definição de pronto do programa

O plano acaba quando:

- zero links mortos nos READMEs de primeiro nível;
- zero nome de arquivo ou diretório com espaço nas pontas;
- catálogo gerado cobre 100% dos feitiços com frontmatter;
- pelo menos quatro responses reais e não vazias;
- nenhum feitiço `battle-tested` sem response;
- CRUD C# antigo marcado `superseded` por um feitiço só, ou justificado por escrito por que continua.

Até lá, a frase honesta no README é: o grimório está em reforma, e o índice do que presta é o catálogo, não a árvore inteira.
