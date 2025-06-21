# 🧙‍♂️ promptologia

**Promptologia** é um grimório moderno de prompts para uso com LLMs em contextos técnicos, sarcásticos e absolutamente desesperados. Ideal para devs cansados, DevOps que conversam com pods e analistas de segurança paranoicos.

> Porque nem todo prompt é só "Explique isso como se eu tivesse 5 anos". Às vezes, é "Explique isso como se eu tivesse feito deploy às 3h da manhã com café vencido".

## 📜 O Manifesto da Promptologia DevComputaria

No caos controlado que chamamos de desenvolvimento de software, onde a única constante é a mudança (e a falta de café depois das 15h), surge a **Promptologia**: a arte arcana e ciência ligeiramente duvidosa de conversar com Inteligências Artificiais para que elas façam o que queremos. Ou algo perto disso.

1.  **A IA é sua Estagiária Superpoderosa (e Ocasionalmente Rebelde):** Trate-a com o respeito que você daria a um gênio júnior com acesso root. Ela pode automatizar o tédio, gerar código que *quase* funciona de primeira e até te ajudar a nomear variáveis (a tarefa mais difícil da computação, como todos sabemos). Mas lembre-se, ela aprendeu com a internet – então, espere o inesperado.
2.  **Clareza Acima de Tudo (Exceto do Sarcasmo):** Prompts devem ser claros. Ou sarcasticamente claros. A IA não tem (ainda) um detector de ironia embutido, mas nós, humanos, apreciamos. Seja específico no que pede, mas sinta-se livre para adicionar um comentário espirituoso. Afinal, rir é o melhor debugging.
3.  **Iterar é Divino (E Necessário):** Seu primeiro prompt raramente será o último. Assim como seu código, ele precisará de refatoração, testes e aquela pequena alteração de última hora que muda tudo. Abrace o ciclo "prompt-erro-ajuste-café-repeat".
4.  **Contexto é Rei (ou Rainha, ou um Comitê Maluco):** Quanto mais contexto você der, menos a IA terá que adivinhar. E поверьте мне (acredite em mim), você não quer que uma IA adivinhe quando se trata do seu deploy de sexta-feira. Forneça exemplos, defina o tom, explique o "porquê" – a menos que o "porquê" seja "porque o chefe mandou".
5.  **Compartilhar é Multiplicar (a Sanidade Coletiva):** Um bom prompt é um tesouro. Um repositório de bons prompts é o mapa do tesouro. Compartilhe suas descobertas, seus fracassos gloriosos e aqueles prompts que, contra todas as probabilidades, funcionaram. A comunidade agradece (e talvez te pague um café).
6.  **Ética? Tentamos:** Lembre-se que LLMs podem gerar coisas... interessantes. Use seus poderes para o bem, ou pelo menos para um mal inofensivo e engraçado. Não peça para a IA dominar o mundo. Ela já tem ideias demais.
7.  **O Humor Salva:** Quando a IA te responder com algo completamente sem sentido pela quinta vez, lembre-se: ela é feita de matemática e texto da internet. Respire fundo, adicione uma pitada de sarcasmo ao seu próximo prompt e tente novamente. Ou vá tomar outro café. Provavelmente o café.

Este é o caminho da Promptologia. Que seus prompts sejam precisos, suas respostas úteis e seu café sempre forte.

## 📚 Estrutura

- `prompts/`: Prompts categorizados por área (dev, devops, secops, humor). Onde a mágica (ou o desespero controlado) acontece.
- `examples/`: Exemplos de respostas geradas por LLMs com esses prompts. Para você ver que não é só com você que a IA às vezes delira.
- `templates/`: Modelos de prompt para quem quiser criar os seus com padrão. Porque reinventar a roda é menos divertido que fazer a IA reinventar para você.
- `README.md`: Você está aqui. Sim, este arquivo. Metalinguagem é chique.

## 📜 Como contribuir

1.  Forka com responsabilidade (ou desespero, não julgamos).
2.  Crie seu prompt seguindo os modelos em `templates/`. Ou não, mas tente manter um mínimo de organização.
3.  Abra uma PR com título sarcástico mas explicativo. Ex: "fix: IA finalmente entende o que é um array".
4.  Responda aos comentários com sabedoria ou memes. Preferencialmente memes.

## 📦 Exemplos de uso

Como invocar os espíritos digitais (também conhecido como usar um prompt):

```bash
curl -X POST https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $SUA_CHAVE_SUPER_SECRETA_DA_IA" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4-turbo-preview", # ou o modelo que estiver na moda
    "messages": [
      {
        "role": "system",
        "content": "Você é um assistente de programação incrivelmente sarcástico, mas útil."
      },
      {
        "role": "user",
        "content": "'$(cat promptologia/prompts/devops/observabilidade.md)'" # Adapte o caminho, claro
      }
    ]
  }'
```
(Sim, esse exemplo de `curl` é mais complicado que pedir pra IA escrever um Olá Mundo. Bem-vindo à Promptologia.)

## 🧠 Engenharia de Prompt: Recursos para Descrentes e Curiosos

Se você acha que "engenharia de prompt" é só um jeito chique de dizer "digitar coisas na IA até funcionar", você está parcialmente certo. Mas existe método na loucura:

*   **Prompt Engineering Guide ([https://www.promptingguide.ai/](https://www.promptingguide.ai/)):** Um guia sério sobre o assunto. Tão sério que quase não tem piada. Quase.
*   **Learn Prompting ([https://learnprompting.org/](https://learnprompting.org/)):** Aprenda a arte de persuadir elétrons a formar frases coerentes.
*   **A Regra de Ouro:** Especificidade > Vagueza. A menos que você queira uma resposta vaga. Aí, ignore esta regra.

## 📖 Licença

WTFPL – Use como quiser, só não culpe a gente se a IA quebrar seu deploy, roubar suas ideias ou começar a escrever poesia existencialista no seu log de produção.

---

Feito com cafeína, logs em tempo real e uma fé inabalável de que a próxima query será a correta.
Um projeto da comunidade [DevComputaria ☕💻].
