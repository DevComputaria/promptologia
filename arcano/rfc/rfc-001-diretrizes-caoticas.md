# RFC-001: As Diretrizes Caóticas da Promptologia DevComputaria

**Status Deste Documento:** Experimental, Altamente Volátil e Sujeito a Alterações Induzidas por Cafeína. Este RFC descreve um conjunto de práticas observadas no campo de batalha da interação com Modelos de Linguagem Grandes (LLMs) pela comunidade DevComputaria. A implementação é opcional, mas o desprezo silencioso por não conformidade é garantido.

**Data:** Quase sexta-feira, 2024

**Autores (Os Culpados):**
*   A Comunidade DevComputaria (aqueles que sobreviveram aos primeiros experimentos)
*   Jules (o escriba relutante desta loucura organizada)

## 1. Resumo

Este RFC estabelece um conjunto de "melhores piores práticas" para a criação, uso e abuso de prompts direcionados a LLMs dentro do ecossistema DevComputaria. O objetivo não é alcançar a perfeição – uma meta fútil e entediante – mas sim maximizar a utilidade, minimizar a frustração existencial e, acima de tudo, manter um nível saudável de sarcasmo técnico enquanto navegamos no admirável mundo novo da IA tagarela. Adotamos o termo "Promptologia" para descrever esta nobre arte de persuadir silício a ser coerente.

## 2. Introdução (A que Problema nos Propomos a Piorar?)

Os LLMs chegaram. Eles são poderosos, onipresentes e, ocasionalmente, completamente desequilibrados. Tentar extrair informações úteis ou ações consistentes deles pode parecer uma tentativa de explicar o paradoxo do bootstrap para um esquilo hiperativo. Este documento visa trazer um *pouco* de método a essa loucura, fornecendo um framework flexível (leia-se: com muitas brechas) para que nós, pobres desenvolvedores, DevOps, SREs e curiosos, possamos colaborar com nossos novos overlords de IA sem perder completamente a sanidade. Ou, pelo menos, documentar nossa descida à insanidade de forma estruturada.

A Promptologia DevComputaria reconhece que:
*   Prompts são código. Código feio, talvez, escrito em linguagem natural bugada, mas código.
*   LLMs são caixas-pretas cheias de surpresas, como uma piñata em um campo minado.
*   O humor é um mecanismo de defesa essencial.

## 3. Princípios (Dogmas Inflexíveis e Sugestões Flexíveis)

Estes são os pilares sobre os quais a Promptologia DevComputaria é (precariamente) construída.

### 3.1. A Diretriz da Clareza Obscura
*   **Dogma:** Seu prompt deve ser tão claro quanto possível para a IA, mas tão obscuro quanto necessário para manter os não iniciados à distância.
*   **Sugestão:** Use linguagem precisa. Evite ambiguidades como se fossem uma reunião de planejamento de sprint às 17h de sexta. A menos, claro, que a ambiguidade seja intencional e parte de um plano maior e mais nefasto.

### 3.2. O Princípio da Iteração Interminável (ou "Tenta de Novo, Idiota")
*   **Dogma:** O primeiro prompt *nunca* é o prompt final. Aceite isso. Chore um pouco. Pegue mais café.
*   **Sugestão:** Encare o versionamento de prompts como faria com qualquer outro artefato de software. `prompt_v1_final.md`, `prompt_v2_final_mesmo.md`, `prompt_v3_agora_vai_confia.md` são todos sinais de um promptologista experiente.

### 3.3. A Lei do Contexto Abundante (Mas Não Entediante)
*   **Dogma:** LLMs têm a memória de um peixinho dourado com TDAH. Forneça contexto suficiente para que eles saibam o que você quer, mas não tanto a ponto de entediá-los e fazê-los divagar sobre a história da fabricação de clipes de papel.
*   **Sugestão:** Use exemplos (few-shot prompting), defina papéis ("Você é um SRE cínico...") e especifique o formato de saída desejado. Se o prompt parecer um romance russo, talvez seja hora de simplificar.

### 3.4. O Axioma do Sarcasmo Construtivo
*   **Dogma:** O sarcasmo é o óleo que lubrifica as engrenagens da DevComputaria. Incorpore-o.
*   **Sugestão:** Embora a IA possa não "entender" o sarcasmo (ainda), os humanos que leem e mantêm os prompts certamente o farão. Um prompt bem-humorado é um prompt mais fácil de manter. E se a IA começar a responder sarcasticamente, saberemos que alcançamos a singularidade.

### 3.5. A Regra da Reutilização Desavergonhada
*   **Dogma:** Nunca escreva um prompt do zero se você pode "pegar emprestado" um que já existe e adaptá-lo.
*   **Sugestão:** Mantenha um grimório (como este repositório!) de prompts testados em batalha. A originalidade é superestimada, especialmente quando há um incêndio na produção.

## 4. Formatos de Prompt (Sugestões, Não Mandamentos)

Embora a anarquia seja tentadora, alguma estrutura ajuda a não transformar tudo num completo pandemônio.

### 4.1. Metadados Essenciais (O Mínimo que Você Deveria se Importar)
*   **Título:** Algo descritivo e, se possível, engraçado.
*   **Categoria:** `dev`, `devops`, `secops`, `humor`, `gerencia_perdidamente_confusa`, etc.
*   **Objetivo:** O que diabos esse prompt tenta fazer?
*   **Input Esperado:** O que a IA precisa comer para funcionar? (código, logs, descrição vaga, sonhos partidos)
*   **Saída Esperada:** O que você espera que a IA regurgite? (código, JSON, um poema, um plano para dominar o mundo)

### 4.2. O Corpo do Prompt (Onde a "Mágica" Acontece)
*   **Persona (Role-playing):** "Você é um pato de borracha sênior..."
*   **Instruções Claras e Diretas:** Use listas, imperativos.
*   **Exemplos (Few-shot):** Se aplicável, mostre à IA o que você quer.
*   **Constraints (Restrições):** "Responda em JSON.", "Não use a palavra 'sinergia'."
*   **Placeholders:** Use `{{VARIAVEL_AQUI}}` para partes que serão substituídas dinamicamente.

### 4.3. Notas Adicionais (Onde Você Confessa Seus Pecados)
*   Dicas de uso, modelos de IA testados, limitações conhecidas, piadas internas.

## 5. Considerações de Segurança (Ou: Como Não Irritar Skynet)

*   **Prompt Injection é Real:** Assim como SQL Injection, mas com mais chances de a IA te xingar de volta. Sanitize inputs se estiver usando dados do usuário para construir prompts. Ou não, e viva perigosamente.
*   **Vazamento de Dados:** Não coloque sua chave da AWS ou os segredos da sua avó no prompt. A IA é tagarela.
*   **Conteúdo Ofensivo/Enviesado:** LLMs são treinados com a internet. Espere o pior, torça pelo melhor. Use técnicas para mitigar, mas não confie cegamente.
*   **Over-Reliance (Dependência Excessiva):** Lembre-se, é uma ferramenta. Se a IA disser para pular da ponte, peça uma segunda opinião. De preferência, humana.

## 6. Considerações sobre o Café (O Combustível da Promptologia)

A Promptologia não funciona sem um suprimento adequado e constante de café.

*   **Tipos Aceitáveis:** Forte, muito forte, "isso ainda é legalmente café?".
*   **Níveis de Cafeína:** Devem ser diretamente proporcionais à complexidade do prompt e inversamente proporcionais à coerência da IA.
*   **Horários:** 24/7. Especialmente durante sessões de debugging de prompt às 3 da manhã.

Este RFC não endossa nenhuma marca específica de café, mas secretamente julgamos quem toma descafeinado.

## 7. Autores (Os Culpados)

Nós, da DevComputaria, coletivamente assumimos a responsabilidade (e nenhuma culpa legal) por este documento. Que ele sirva como um farol de sanidade questionável na névoa da revolução da IA.

Ou, pelo menos, que gere algumas risadas antes que os robôs tomem nossos empregos.
---
**FIM DO RFC-001**
(Até alguém ter uma ideia melhor, ou o café acabar)
