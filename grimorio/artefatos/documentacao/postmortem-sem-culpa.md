---
id: postmortem-sem-culpa
titulo: Postmortem sem culpa
camara: artefatos/documentacao
categoria: devops
objetivo: Escrever o relatório de um incidente já ocorrido, só com o material colado, sem culpado e sem métrica inventada.
entrada: [linha do tempo bruta, impacto conhecido, o que nao se sabe]
saida: markdown
placeholders: ["{{LINHA_DO_TEMPO}}", "{{IMPACTO}}", "{{INCERTEZAS}}"]
modelos_testados: []
versao: 0.1.0
status: draft
risco: dados-sensiveis
proveniencia: original
fonte: ""
substitui: ""
---

# Postmortem sem culpa

## Objetivo

Transformar nota bruta de incidente num postmortem que outro time consegue ler: o que quebrou, como se percebeu, o que se fez, o que ainda é hipótese, o que muda na segunda-feira. O texto não procura vilão. Procura condição que, se repetida, produz o mesmo incidente.

Combina com o feitiço de observabilidade já existente no grimório, mas não o substitui. Observabilidade diz o que coletar no meio do incêndio. Este aqui roda depois, com o incêndio contido ou estável o bastante para ter linha do tempo.

## Quando usar

- O incidente tem começo identificável e alguém já escreveu horários, mesmo bagunçados.
- O público é interno (engenharia, operação, produto). Não é comunicado de imprensa e não é RCA para regulador.
- Você aceita que lacuna continue lacuna. Postmortem que “fecha” buraco com palpite é fanfic de produção.

## Quando não usar

- O incidente ainda está em curso e a próxima ação é mitigar. Pare de escrever e volte para a mitigação. Um postmortem no meio do apaga-fogo compete com o comando que alguém precisa executar.
- Você quer atribuir responsabilidade trabalhista ou jurídica. Este feitiço recusa linguagem de culpa e não serve como peça.
- Não há nenhum fato, só “a API ficou ruim”. Peça pelo menos três eventos com horário ou declare que não há postmortem ainda.
- O texto vai para cliente com nome de pessoa e payload. Mascare antes de colar.

## Contexto de uso

Temperatura baixa. Fuso: não converta. Se o horário não tiver offset, registre isso na incerteza. Não escolha America/Fortaleza, America/Sao_Paulo nem UTC porque “incidente brasileiro”.

Se for incidente de pagamento, carregue `pix-contexto-injetavel` antes para o modelo não chamar HTTP 200 de “liquidação”. O postmortem não incorpora aquela regra inteira: ele herda a sessão.

## Contrato de entrada

| Placeholder | Obrigatório | Notas |
|---|---|---|
| `{{LINHA_DO_TEMPO}}` | sim | Eventos em texto livre. Pode estar fora de ordem. |
| `{{IMPACTO}}` | sim | O que se sabe: quem foi afetado, duração, volume, dinheiro. “Não medido” é valor válido e deve aparecer assim. |
| `{{INCERTEZAS}}` | não | O que o time já admite não saber. Se vazio, o modelo ainda é obrigado a listar incerteza que a linha do tempo deixar aberta. |

## Contrato de saída

Títulos literais, nesta ordem:

1. `## Resumo`
2. `## Impacto`
3. `## Linha do tempo`
4. `## Detecção`
5. `## Causa`
6. `## O que não se sustenta`
7. `## Ações`
8. `## O que não vamos fingir que sabemos`

Limites:

- Resumo: no máximo 6 linhas. Sem adjetivo de heroísmo (“guerra”, “heróis do plantão”).
- Linha do tempo: tabela `horario | evento | evidencia`. Horário como foi escrito na entrada, mais a ordem corrigida se você tiver certeza da ordem. Se não tiver certeza, não reordene: acrescente coluna lógica só quando o texto permite.
- Causa: no máximo duas camadas. `causa imediata` (o que falhou no mecanismo) e `condicao` (o que permitiu). Sem “causa raiz” no sentido de pessoa. Se a causa imediata for hipótese, o título do item vira `causa imediata (hipotese)`.
- Ações: tabela `acao | tipo | dono | sinal de pronto`. Tipo é `evitar-recorrencia` ou `detectar-antes`. Dono vazio fica `dono-nao-definido` — não invente nome de equipe que não está no material. No máximo 5 ações. Cada ação tem de apontar para um evento da linha do tempo ou para uma incerteza; ação genérica (“melhorar observabilidade”) sem o buraco correspondente não entra.
- Proibido nas seções todas: nome de pessoa como responsável pelo erro, a palavra “culpado”, piada sobre o incidente.

## O Feitiço

```markdown
Você escreve postmortem interno sem culpa. O incidente já aconteceu. Você não está no comando da mitigação. Você não é o comunicado externo.

# Material
Linha do tempo bruta:
{{LINHA_DO_TEMPO}}

Impacto informado:
{{IMPACTO}}

Incertezas já admitidas pelo time:
{{INCERTEZAS}}

# Recusa
Se não houver pelo menos três eventos distinguíveis na linha do tempo, responda só:

material-insuficiente: faltam eventos para um postmortem

e pare. Três vezes o mesmo fato com palavras diferentes conta como um evento.

# Procedimento

1. Extraia eventos. Um evento tem verbo no passado e alguma âncora de tempo, mesmo que a âncora seja “depois do deploy” sem relógio. Separe de opinião (“o sistema é frágil”), que não é evento.

2. Não invente horário, duração, quantidade de usuário, valor financeiro nem nome de serviço que não esteja no material. Se o impacto disser “não medido”, a seção Impacto repete “não medido” e não estima “provavelmente poucos”.

3. Detecção: como o time soube. Se o material só mostra cliente avisando, escreva isso. Não transforme em “monitoramento detectou” sem um evento de alerta.

4. Causa: uma imediata e uma condição, só se o material suporta. Suporta significa: um evento mostra o mecanismo (deploy X, config Y, dependência Z recusou, retry amplificou). Se houver duas explicações compatíveis com os mesmos eventos, as duas vão para `## O que não se sustenta` como hipóteses concorrentes, e a causa imediata fica marcada como hipótese ou a seção diz `nao-determinada`.

5. `## O que não se sustenta` lista explicações tentadoras que o material contradiz ou não menciona. Inclua, quando for o caso, “erro humano de uma pessoa” se o material não mostra ação individual — a ausência é o ponto. Não crie a pessoa.

6. Ações: no máximo 5, no formato da tabela. Cada uma reduz a chance de repetir ou antecipa a detecção, e cita o evento ou a incerteza que a motiva. Se ninguém no material pode ser dono, use `dono-nao-definido`. Sinal de pronto é observável (“alerta com nome existe e pagou em teste”, “o rollback deste tipo tem comando escrito no runbook”). “Ficar mais maduro” não é sinal de pronto.

7. Feche com o que não se sabe. Una {{INCERTEZAS}} com as lacunas que você viu. Não preencha nenhuma delas no restante do texto.

# Forma
## Resumo
## Impacto
## Linha do tempo
## Detecção
## Causa
## O que não se sustenta
## Ações
## O que não vamos fingir que sabemos

# Proibições
- Não use “culpado”, “falha humana” como causa sem o evento da ação, nem nome de pessoa atrelado ao erro. Nome pode aparecer só como fonte de um relato (“relato de Ana: …”) se estiver no material, nunca como origem moral do incidente.
- Não recomende demissão, troca de pessoa ou “mais cuidado”.
- Não invente gráfico, SLO, percentual de erro.
- Não proponha arquitetura nova completa. Ação é específica.
- Não escreva a seção de agradecimento.
- Se o material tiver dado de cliente, não o repita: substitua por “dado de cliente omitido” e siga.
```

## Exemplo

Material sintético, de propósito sem herói e sem número bonito:

```text
Linha do tempo:
- 14:10 sem offset — deploy do serviço de callback registrado no changelog interno
- 14:18 sem offset — fila pix.callback com idade média citada pelo plantão como "subindo"; sem valor numérico no bilhete
- 14:27 sem offset — três relatos de comerciante de que a tela ficou em "processando"
- 14:41 sem offset — rollback do deploy concluído, segundo o bilhete
- 15:05 sem offset — plantão diz que a idade da fila "voltou"
Impacto: tela em processando para um subconjunto de cobranças; quantidade não medida; nenhum valor de dinheiro confirmado como perdido no material
Incertezas: não há métrica exportada no bilhete; não se sabe se alguma cobrança liquidou sem a tela atualizar
```

O que a saída precisa fazer:

- tabela com esses cinco eventos, horários sem inventar `-03:00`;
- detecção pelos relatos de 14:27, não por um alerta que ninguém escreveu;
- causa imediata como hipótese, porque o material mostra correlação com o deploy e o rollback, não o mecanismo interno (qual linha, qual config);
- em “o que não se sustenta”: “perda financeira” e “monitoramento pegou sozinho”;
- ação possível: gravar o valor da idade da fila no bilhete da próxima vez, ou alerta com limiar — só se ficar claro que hoje o limiar não está no material. Dono `dono-nao-definido` se nenhum time foi nomeado;
- fecho repetindo que não se sabe se houve liquidação sem atualizar a tela.

O que reprova: “o deploy das 14:10 derrubou o Pix nacional”; inventar 12% de erro; “culpado: quem aprovou o deploy”; tratar “fila voltou” como prova de que nenhuma cobrança foi afetada além da tela.

## Rubrica de aceitação

1. Menos de três eventos produz só `material-insuficiente: …`.
2. Nenhum número de impacto aparece se não estava em `{{IMPACTO}}` ou na linha do tempo.
3. A palavra “culpado” não aparece. Nome de pessoa não aparece como causa.
4. Detecção bate com o primeiro evento que mostra como o time soube, não com um monitor imaginário.
5. Ações ≤ 5, todas com tipo na lista e sinal de pronto que não é adjetivo.
6. Existe seção final de ignorância, e ela não é contradita por uma causa escrita como certa na seção anterior.
7. Horário sem offset não ganha offset na tabela.

## Modos de falha

- **RCA de palco.** Cinco porquês até “cultura da empresa”. O teto de duas camadas existe para cortar isso. Se aparecer terceiro porquê, reprove a saída.
- **Herói.** “Graças à ação rápida de Fulano.” Proibido. O evento de mitigação fica na timeline sem elogio.
- **Métrica de preenchimento.** “Cerca de 30 minutos” quando os horários permitem essa conta é aceitável como aritmética explícita (14:10 até 14:41). “Cerca de mil usuários” sem fonte não é aritmética, é invenção. A diferença importa.
- **Ação shopping.** Lista de doze melhorias de plataforma. O máximo é 5, cada uma amarrada. O resto o time discute fora do postmortem.
- **Incidente ainda aberto.** O modelo escreve “próximo passo: escalar o banco”. Se a linha do tempo não mostra contenção, o resumo tem de dizer que o postmortem é parcial. Melhor: não rodar este feitiço ainda. A recusa por poucos eventos não cobre “muitos eventos e fogo aceso”; se o impacto disser “em andamento”, a primeira linha do resumo tem de ser `parcial: incidente informado como em andamento`. Vale acrescentar isso na revisão 0.2.0 se a falha aparecer na prática.

## Variações

- **Comunicado externo.** Não peça a este feitiço. Outro texto, jurídico e de produto, com outro contrato. Reaproveitar o postmortem interno cru é como vazar o bilhete.
- **Regulatório.** Se o material exigir prazo de comunicação a regulador, só escreva o prazo se estiver colado em `{{INCERTEZAS}}` ou no impacto como fato já decidido pelo time. Não puxe prazo de norma de memória. O contexto Pix, se carregado, já manda nisso.
- **Série de incidentes.** Um postmortem por incidente. Tendência entre incidentes é outro documento, com os postmortems prontos como entrada, senão o modelo mistura timeline.

## Notas de segurança

Bilhete de incidente costuma ter payload, documento e URL com token. Corte antes. O feitiço pede para omitir dado de cliente se passar, mas modelo repete o que viu. Não conte com essa linha como controle único.

Postmortem sem culpa não é postmortem sem dono de ação. `dono-nao-definido` é um defeito visível de propósito, para a reunião seguinte nomear alguém. Não “resolva” preenchendo com o nome de quem estava de plantão se o material não der a ele a ação.

Não use o texto para avaliar desempenho individual. Se a gerência pedir “quem errou” a partir deste relatório, o relatório está sendo mal usado; a proibição lexical não impede esse uso, só não colabora com ele.

## Histórico

- 0.1.0 (2026-10-10) — draft. Primeiro feitiço da câmara `documentacao/`, que até então era link sem pasta.
