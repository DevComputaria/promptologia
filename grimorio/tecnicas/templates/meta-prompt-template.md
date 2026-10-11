---
id: "meta-prompt-template"
titulo: "Meta-prompt"
camara: "tecnicas"
categoria: "harness"
objetivo: "Checklist para construir um prompt antes de escrevê-lo."
entrada: ["objetivo", "público", "formato"]
saida: "markdown"
placeholders: ["{{CATEGORIA_DO_SEU_PROMPT}}", "{{CONTEXTO_ADICIONAL}}", "{{CONTEXTO_ADICIONAL_AQUI_SE_NECESSARIO}}", "{{DADOS_AQUI}}", "{{DESCRICAO_DO_FORMATO_DA_RESPOSTA_OU_EXEMPLO_DE_FORMATO}}", "{{DETALHES_DO_INPUT}}", "{{DETALHES_DO_OUTPUT_ESPERADO}}", "{{EXEMPLO_INPUT_1}}", "{{EXEMPLO_INPUT_2}}", "{{EXEMPLO_OUTPUT_1}}", "{{EXEMPLO_OUTPUT_2}}", "{{INPUT_ESPERADO_RESUMIDO}}", "{{INSTRUCAO_1}}", "{{INSTRUCAO_1_DO_SEU_PROMPT}}", "{{INSTRUCAO_2}}", "{{INSTRUCAO_2_DO_SEU_PROMPT}}", "{{NOME_DA_VARIAVEL}}", "{{NOTA_1_PARA_USUARIOS_DO_SEU_PROMPT}}", "{{NOTA_2_PARA_USUARIOS_DO_SEU_PROMPT}}", "{{OBJETIVO_DO_SEU_PROMPT}}", "{{OBJETIVO_DO_SEU_PROMPT_RESUMIDO}}", "{{OUTPUT_ESPERADO_RESUMIDO}}", "{{PERSONA_DA_IA}}", "{{PERSONA_DA_IA_AQUI}}", "{{PLACEHOLDER_1}}", "{{PLACEHOLDER_2}}", "{{PLACEHOLDER_PARA_INPUT_PRINCIPAL_DO_USUARIO}}", "{{PUBLICO_ALVO_DA_RESPOSTA}}", "{{REGRAS_E_RESTRICOES}}", "{{RESTRICAO_1}}", "{{RESTRICAO_2}}", "{{SECAO_DE_EXEMPLOS_FEW_SHOT_SE_APLICAVEL}}", "{{SUB_INSTRUCAO_A_SE_HOUVER}}", "{{TITULO_DO_SEU_PROMPT}}"]
modelos_testados: []
versao: "0.1.0"
status: "draft"
risco: "nenhum"
proveniencia: "original"
fonte: ""
substitui: ""
---

#  META-PROMPT: Seu Guia para Construir Prompts Que (Geralmente) Funcionam

Este é um **meta-prompt**, um prompt sobre como criar prompts. Use-o como um checklist ou um guia de reflexão para construir seus próprios prompts eficazes, especialmente ao interagir com LLMs avançados como os da família GPT. Lembre-se, a clareza e a especificidade são suas melhores amigas (depois do café, claro).

---

## 🧐 Seção 1: O Básico Iluminado (Fundamentos do Prompt)

Pense nisto antes de escrever uma única linha do seu prompt real.

1.  **Qual é o OBJETIVO PRINCIPAL do seu prompt?**
    *   O que você quer que a IA *faça*? (Gerar código, resumir texto, responder a uma pergunta, classificar itens, etc.)
    *   Seja específico. "Preciso de ajuda com Python" é vago. "Preciso de uma função Python que receba uma lista de strings e retorne uma lista com as strings em maiúsculas e ordenadas" é melhor.
    *   *Seu Objetivo Aqui:* `{{OBJETIVO_DO_SEU_PROMPT}}`

2.  **Quem é o PÚBLICO-ALVO da resposta da IA?**
    *   É para você? Para um colega técnico? Para um cliente não técnico? Para o seu gato (não julgamos)?
    *   Isso influencia o tom, a complexidade e o formato da resposta.
    *   *Seu Público-Alvo Aqui:* `{{PUBLICO_ALVO_DA_RESPOSTA}}`

3.  **Qual é o INPUT que a IA receberá?**
    *   A IA precisará de dados específicos? Código? Um texto longo? Uma pergunta simples?
    *   Como esses dados serão fornecidos? (Diretamente no prompt, como um placeholder `{{DADOS_AQUI}}`, etc.)
    *   *Input Detalhado Aqui:* `{{DETALHES_DO_INPUT}}`

4.  **Qual é a SAÍDA ESPERADA?**
    *   Formato: JSON? Markdown? Texto corrido? Uma lista? Código em uma linguagem específica?
    *   Estrutura: Se JSON, quais chaves? Se Markdown, quais seções?
    *   Extensão: Curto e direto? Detalhado e explicativo?
    *   Tom: Formal? Informal? Sarcástico? Empático?
    *   *Output Detalhado Aqui:* `{{DETALHES_DO_OUTPUT_ESPERADO}}`

---

## 🎭 Seção 2: Definindo a Persona e o Contexto (Role-Playing para IAs)

Dar à IA um "papel" pode melhorar drasticamente a qualidade da resposta.

1.  **Que PERSONA/PAPEL a IA deve assumir?**
    *   "Você é um desenvolvedor Python sênior..."
    *   "Você é um especialista em segurança de APIs..."
    *   "Você é um comediante explicando computação quântica..."
    *   "Você é um pato de borracha que ouve os problemas dos desenvolvedores..."
    *   *Persona da IA Aqui:* `{{PERSONA_DA_IA}}`

2.  **Qual CONTEXTO relevante você pode fornecer?**
    *   Informações de fundo sobre o problema.
    *   Restrições importantes (ex: "Não use bibliotecas externas", "A solução deve ser compatível com Python 3.7").
    *   O "porquê" da tarefa, se ajudar a IA a entender melhor o objetivo.
    *   *Contexto Relevante Aqui:* `{{CONTEXTO_ADICIONAL}}`

---

## 📝 Seção 3: Estruturando o Prompt (A Arquitetura da Magia)

Como você vai organizar as instruções para a IA.

1.  **Instruções CLARAS e DIRETAS:**
    *   Use linguagem imperativa ("Faça X", "Gere Y", "Liste Z").
    *   Numere os passos se a tarefa for complexa.
    *   Use delimitadores (como ```` ``` ````, `###`, `<tags>`) para separar seções do seu prompt ou para indicar onde o input do usuário entra, se for o caso.
    *   *Esboço das Instruções Aqui:*
        1.  `{{INSTRUCAO_1}}`
        2.  `{{INSTRUCAO_2}}`
        3.  ...

2.  **EXEMPLOS (Few-Shot Prompting):**
    *   Mostrar é muitas vezes melhor que dizer. Forneça 1 a 3 exemplos de input e output desejado.
    *   Isso ajuda a IA a entender o formato, o estilo e o nível de detalhe esperado.
    *   *Exemplos (se aplicável):*
        *   Input: `{{EXEMPLO_INPUT_1}}` -> Output: `{{EXEMPLO_OUTPUT_1}}`
        *   Input: `{{EXEMPLO_INPUT_2}}` -> Output: `{{EXEMPLO_OUTPUT_2}}`

3.  **REGRAS e RESTRIÇÕES:**
    *   O que a IA NÃO deve fazer? ("Não inclua explicações longas", "Não use gírias").
    *   Existem palavras-chave ou frases a serem evitadas ou incluídas?
    *   *Regras e Restrições Aqui:* `{{REGRAS_E_RESTRICOES}}`

4.  **PLACEHOLDERS para Variáveis:**
    *   Use um formato consistente para placeholders que serão substituídos por dados reais (ex: `{{NOME_DA_VARIAVEL}}`, `<<INPUT_DO_USUARIO>>`).
    *   Isso torna seu prompt reutilizável.
    *   *Placeholders Usados:* `{{PLACEHOLDER_1}}`, `{{PLACEHOLDER_2}}`

---

## ✨ Seção 4: Refinamento e Teste (A Arte da Iteração Dolorosa mas Necessária)

Seu primeiro prompt raramente é o melhor.

1.  **Simplicidade Primeiro:** Comece com um prompt mais simples e adicione complexidade gradualmente.
2.  **Teste com Diferentes Formulações:** Às vezes, mudar uma frase ou a ordem das instruções faz uma grande diferença.
3.  **Controle de Temperatura/Criatividade (se a plataforma permitir):**
    *   Temperaturas mais baixas (ex: 0.2) para respostas mais factuais e determinísticas.
    *   Temperaturas mais altas (ex: 0.8) para respostas mais criativas ou diversas.
4.  **Peça à IA para Explicar (Chain-of-Thought):** Se a resposta estiver errada, você pode pedir à IA para "pensar passo a passo" ou "explicar seu raciocínio" para entender onde as coisas deram errado. Isso pode até ser parte do seu prompt principal para tarefas complexas.
5.  **Itere, Itere, Itere:** Guarde versões do seu prompt. O que funcionou? O que não funcionou? Por quê? (Sim, é quase como debuggar código, só que com um compilador muito mais temperamental).

---

## 📜 Template Final do Seu Novo Prompt (Preencha com base nas seções acima)

```markdown
# 🧠 {{TITULO_DO_SEU_PROMPT}}

**Categoria:** {{CATEGORIA_DO_SEU_PROMPT}}
**Objetivo:** {{OBJETIVO_DO_SEU_PROMPT_RESUMIDO}}
**Input esperado:** {{INPUT_ESPERADO_RESUMIDO}}
**Saída esperada:** {{OUTPUT_ESPERADO_RESUMIDO}}

---

## 🔮 Prompt

{{PERSONA_DA_IA_AQUI}}

{{CONTEXTO_ADICIONAL_AQUI_SE_NECESSARIO}}

**Siga estas instruções:**
1.  {{INSTRUCAO_1_DO_SEU_PROMPT}}
2.  {{INSTRUCAO_2_DO_SEU_PROMPT}}
    {{SUB_INSTRUCAO_A_SE_HOUVER}}
3.  ...

{{SECAO_DE_EXEMPLOS_FEW_SHOT_SE_APLICAVEL}}

**Input do Usuário:**
{{PLACEHOLDER_PARA_INPUT_PRINCIPAL_DO_USUARIO}}

**Formato da Resposta:**
{{DESCRICAO_DO_FORMATO_DA_RESPOSTA_OU_EXEMPLO_DE_FORMATO}}

**Restrições Adicionais:**
- {{RESTRICAO_1}}
- {{RESTRICAO_2}}

---

## 💡 Notas
- {{NOTA_1_PARA_USUARIOS_DO_SEU_PROMPT}}
- {{NOTA_2_PARA_USUARIOS_DO_SEU_PROMPT}}
```

Lembre-se: A promptologia é uma ciência experimental com uma pitada de arte obscura e muita cafeína. Boa sorte, e que seus tokens sejam bem gastos!
