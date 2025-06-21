# 🧙‍♂️ promptologia

**Promptologia** é um grimório moderno de prompts para uso com LLMs em contextos técnicos, sarcásticos e absolutamente desesperados. Ideal para devs cansados, DevOps que conversam com pods e analistas de segurança paranoicos.

> Porque nem todo prompt é só "Explique isso como se eu tivesse 5 anos". Às vezes, é "Explique isso como se eu tivesse feito deploy às 3h da manhã com café vencido".

## 📚 Estrutura

- `prompts/`: Prompts categorizados por área (dev, devops, secops, humor).
- `examples/`: Exemplos de respostas geradas por LLMs com esses prompts.
- `templates/`: Modelos de prompt para quem quiser criar os seus com padrão.
- `README.md`: Você está aqui.

## 📜 Como contribuir

1. Forka com responsabilidade (ou desespero).
2. Crie seu prompt seguindo os modelos em `templates/`.
3. Abra uma PR com título sarcástico mas explicativo.
4. Responda aos comentários com sabedoria ou memes.

## 📦 Exemplos de uso

```bash
curl -X POST https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -d @prompts/devops/observabilidade.md
```

## 📖 Licença

WTFPL – Use como quiser, só não culpe a gente se a IA quebrar seu deploy.

---

Feito com cafeína e logs em tempo real.
Um projeto da comunidade [DevComputaria ☕💻].
