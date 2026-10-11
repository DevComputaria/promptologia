---
id: "csharp-unittest-controller"
titulo: "Testes de controller C#"
camara: "artefatos/codigo"
categoria: "dev"
objetivo: "Gerar testes de controller para sucesso, NotFound e BadRequest."
entrada: ["código do controller", "framework"]
saida: "csharp"
placeholders: ["{{CODIGO_DO_CONTROLLER_AQUI}}", "{{FRAMEWORK_DE_TESTE}}", "{{NomeDoController}}"]
modelos_testados: []
versao: "0.1.0"
status: "draft"
risco: "nenhum"
proveniencia: "original"
fonte: ""
substitui: ""
---

# 🧠 Gerador de Testes Unitários para Controllers C# (Estilo TDD Preguiçoso)

**Categoria:** dev / csharp / testing
**Objetivo:** Criar uma classe de testes unitários (usando MSTest, NUnit ou xUnit) para um controller C# WebAPI, focando em cobrir os cenários básicos: sucesso (OK), não encontrado (NotFound) e requisição inválida (BadRequest). Porque testar é preciso, mas ninguém disse que precisa ser doloroso.
**Input esperado:** Código do Controller C# a ser testado, e o framework de teste desejado (MSTest, NUnit, xUnit).
**Saída esperada:** Código C# da classe de teste com métodos de teste para os principais cenários dos actions públicos do controller.

---

## 🔮 Prompt

Você é um engenheiro de software que acredita fervorosamente em testes, mas também valoriza seu tempo (e sanidade). Sua missão é gerar uma classe de testes unitários para o seguinte Controller C# WebAPI, usando o framework de teste especificado. O foco é na cobertura dos "happy paths" e dos erros mais comuns (NotFound, BadRequest).

**Framework de Teste (MSTest, NUnit, ou xUnit):** `{{FRAMEWORK_DE_TESTE}}`

**Código do Controller C#:**
```csharp
{{CODIGO_DO_CONTROLLER_AQUI}}
```

**Instruções:**
1.  Crie uma classe de teste com o nome `{{NomeDoController}}Tests`.
2.  Use mocks (ex: Moq) para as dependências do controller (serviços, repositórios).
3.  Para cada Action pública no controller:
    *   Crie um método de teste para o cenário de sucesso (retorno HTTP 200 OK ou 201 Created). Verifique o tipo do resultado (ex: `OkObjectResult`, `CreatedAtActionResult`) e, se aplicável, o valor retornado.
    *   Se o Action busca por ID ou atualiza/deleta, crie um teste para o cenário "não encontrado" (HTTP 404 NotFound).
    *   Se o Action recebe um modelo e pode ter `ModelState` inválido, crie um teste para o cenário de "requisição inválida" (HTTP 400 BadRequest).
4.  Use os atributos específicos do framework de teste escolhido (ex: `[TestMethod]` para MSTest, `[Test]` para NUnit, `[Fact]` para xUnit).
5.  Adicione um comentário no início da classe de teste, algo como: "Testes existem para que eu possa dormir à noite. Ou pelo menos tentar."

Responda apenas com o código C# da classe de testes. Não inclua o código do controller original na resposta. E que os testes passem de primeira (sabemos que não vão, mas sonhar é de graça).

---

## 💡 Notas
- Este prompt assume que você tem um framework de mock como Moq instalado no seu projeto de teste.
- A complexidade dos mocks e asserções pode variar muito. Este prompt foca no básico para dar um pontapé inicial.
- Lembre-se de que testar `ModelState` programaticamente requer adicionar erros ao `ModelState` do controller no setup do teste. Ex: `_controller.ModelState.AddModelError("chave", "erro");`
- "Cobrir tudo" é uma utopia. Foque no que agrega mais valor e reduz mais risco. E depois vá tomar um café. Você merece.
