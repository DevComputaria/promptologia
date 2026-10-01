---
id: artefato.codigo.csharp-unittest-controller
titulo: Gerador de Testes Unitários para Controllers C#
camara: artefatos/codigo
status: rascunho
fonte: []
modelos_testados: []
variaveis:
  - name: framework_de_teste
    required: true
  - name: codigo_do_controller
    required: true
  - name: nome_do_controller
    required: true
saida: codigo-csharp
prompt_id: null
atualizado: 2026-09-30
---

# 🧠 Gerador de Testes Unitários para Controllers C# (Estilo TDD Preguiçoso)

## 🎯 Objetivo

Criar uma classe de testes unitários com MSTest, NUnit ou xUnit para um controller C# Web API, cobrindo sucesso, recurso não encontrado e requisição inválida.

## 🧠 Contexto de Uso

Forneça o controller e o framework desejado. A saída é somente o código C# da classe de testes para as actions públicas.

## 📝 O Feitiço (Prompt)

Você é um engenheiro de software que acredita fervorosamente em testes, mas também valoriza seu tempo (e sanidade). Sua missão é gerar uma classe de testes unitários para o seguinte Controller C# WebAPI, usando o framework de teste especificado. O foco é na cobertura dos "happy paths" e dos erros mais comuns (NotFound, BadRequest).

**Framework de Teste (MSTest, NUnit, ou xUnit):** `{{framework_de_teste}}`

**Código do Controller C#:**
```csharp
{{codigo_do_controller}}
```

**Instruções:**
1.  Crie uma classe de teste com o nome `{{nome_do_controller}}Tests`.
2.  Use mocks (ex: Moq) para as dependências do controller (serviços, repositórios).
3.  Para cada Action pública no controller:
    *   Crie um método de teste para o cenário de sucesso (retorno HTTP 200 OK ou 201 Created). Verifique o tipo do resultado (ex: `OkObjectResult`, `CreatedAtActionResult`) e, se aplicável, o valor retornado.
    *   Se o Action busca por ID ou atualiza/deleta, crie um teste para o cenário "não encontrado" (HTTP 404 NotFound).
    *   Se o Action recebe um modelo e pode ter `ModelState` inválido, crie um teste para o cenário de "requisição inválida" (HTTP 400 BadRequest).
4.  Use os atributos específicos do framework de teste escolhido (ex: `[TestMethod]` para MSTest, `[Test]` para NUnit, `[Fact]` para xUnit).
5.  Adicione um comentário no início da classe de teste, algo como: "Testes existem para que eu possa dormir à noite. Ou pelo menos tentar."

Responda apenas com o código C# da classe de testes. Não inclua o código do controller original na resposta. E que os testes passem de primeira (sabemos que não vão, mas sonhar é de graça).

---

## 💡 Dicas e Variações
- Este prompt assume que você tem um framework de mock como Moq instalado no seu projeto de teste.
- A complexidade dos mocks e asserções pode variar muito. Este prompt foca no básico para dar um pontapé inicial.
- Lembre-se de que testar `ModelState` programaticamente requer adicionar erros ao `ModelState` do controller no setup do teste. Ex: `_controller.ModelState.AddModelError("chave", "erro");`
- "Cobrir tudo" é uma utopia. Foque no que agrega mais valor e reduz mais risco. E depois vá tomar um café. Você merece.
