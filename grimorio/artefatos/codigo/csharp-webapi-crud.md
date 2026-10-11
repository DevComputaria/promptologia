---
id: "csharp-webapi-crud"
titulo: "Controller CRUD C#"
camara: "artefatos/codigo"
categoria: "dev"
objetivo: "Gerar um controller CRUD assíncrono para uma entidade."
entrada: ["nome da entidade", "serviço opcional"]
saida: "csharp"
placeholders: ["{{NOME_DA_ENTIDADE}}", "{{NOME_DO_SERVICO_OPCIONAL}}", "{{NomeDaEntidadeEmMinusculo}}"]
modelos_testados: []
versao: "0.1.0"
status: "draft"
risco: "nenhum"
proveniencia: "original"
fonte: ""
substitui: ""
---

# 🧠 Gerador de Endpoints CRUD C# WebAPI (Com Cheiro de Café Fresco)

**Categoria:** dev / csharp / webapi
**Objetivo:** Gerar o esqueleto de um controller C# WebAPI com endpoints CRUD (Create, Read, Update, Delete) para uma entidade específica, incluindo o básico de injeção de dependência e async/await, porque ninguém merece código blocante em 2024.
**Input esperado:** Nome da entidade (ex: "Produto", "Usuario"), e opcionalmente, o nome do serviço/repositório a ser injetado (ex: "IProdutoService").
**Saída esperada:** Código C# de um controller com os métodos GET (todos e por ID), POST, PUT e DELETE, utilizando `IActionResult` ou `ActionResult<T>` e chamadas assíncronas.

---

## 🔮 Prompt

Você é um desenvolvedor C# .NET sênior, especialista em construir WebAPIs robustas e escaláveis, e está levemente viciado em café. Sua missão é gerar um Controller para uma API RESTful com as quatro operações básicas (CRUD) para a entidade fornecida.

**Entidade:** `{{NOME_DA_ENTIDADE}}`
**Serviço/Repositório (opcional, se não fornecido, use `I{{NOME_DA_ENTIDADE}}Service`):** `{{NOME_DO_SERVICO_OPCIONAL}}`

**Requisitos:**
1.  Use `[ApiController]` e `[Route("api/[controller]")]`.
2.  Injete a interface do serviço/repositório no construtor.
3.  Implemente os seguintes endpoints assíncronos:
    *   `GET api/{{NomeDaEntidadeEmMinusculo}}`: Retorna todos os itens.
    *   `GET api/{{NomeDaEntidadeEmMinusculo}}/{id}`: Retorna um item por ID.
    *   `POST api/{{NomeDaEntidadeEmMinusculo}}`: Cria um novo item.
    *   `PUT api/{{NomeDaEntidadeEmMinusculo}}/{id}`: Atualiza um item existente.
    *   `DELETE api/{{NomeDaEntidadeEmMinusculo}}/{id}`: Deleta um item.
4.  Use `IActionResult` ou `ActionResult<T>` como tipo de retorno.
5.  Inclua tratamento básico para "não encontrado" (NotFound) nos endpoints que operam por ID.
6.  Adicione um comentário espirituoso sobre a alegria de escrever CRUDs no início do arquivo.

Responda apenas com o código C# do controller. Não precisa da definição da entidade nem do serviço, só o controller mesmo. Que São Stroustrup nos proteja do `OutOfMemoryException`.

---

## 💡 Notas
- Lembre-se de criar a interface `I{{NOME_DA_ENTIDADE}}Service` e sua implementação separadamente. Isso aqui é só o controller, não fazemos milagres (só com muito café).
- Ideal para acelerar o início de novas APIs ou para quando a preguiça de escrever boilerplate bate forte.
- Testado com .NET 6+, mas deve funcionar com versões mais recentes (a menos que a Microsoft decida mudar tudo de novo, o que é sempre uma possibilidade).
