# 📋 SpecKit: O Livro das Especificações

O **SpecKit** é a nossa língua franca para falar de software com humanos e, principalmente, com IAs. Antes de invocar um demônio (ou uma IA) para escrever código, você precisa desenhar o círculo de invocação. Esses templates são os nossos diagramas de giz.

## 🧙 Por que usar o SpecKit?

Especificações são o contexto definitivo. Fornecer uma especificação estruturada para um LLM reduz drasticamente as alucinações e aumenta a precisão do código gerado.

## 📂 O que temos aqui?

*   **[Templates](./templates/)**: Modelos em branco prontos para serem preenchidos.
    *   *O Pergaminho da Funcionalidade*: Para histórias de usuário e requisitos.
    *   *O Tomo da API*: Para definições de endpoints e contratos.
    *   *As Tábuas da Regra de Negócio*: Para lógica complexa e restrições.
*   **[Exemplos](./exemplos/)**: Especificações preenchidas para servir de inspiração.

## 🚀 Como usar

1.  Escolha um **[Template](./templates/)**.
2.  Preencha-o com os detalhes do seu problema.
3.  Use um dos prompts de integração em **[grimorio/tecnicas/speckit-integration/](../../grimorio/tecnicas/speckit-integration/README.md)** para alimentar a IA com esta especificação.
