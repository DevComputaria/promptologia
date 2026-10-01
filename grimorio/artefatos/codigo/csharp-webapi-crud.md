---
id: artefato.codigo.csharp-webapi-crud
titulo: Gerador de Endpoints CRUD C# WebAPI
camara: artefatos/codigo
status: rascunho
fonte: []
modelos_testados: []
variaveis:
  - name: nome_da_entidade
    required: true
  - name: nome_do_servico_opcional
    required: false
saida: codigo-csharp
prompt_id: null
atualizado: 2026-09-30
---

# 🧠 Gerador de Endpoints CRUD C# WebAPI (Com Cheiro de Café Fresco)

## 🎯 Objetivo

Gerar o esqueleto de um controller C# Web API com endpoints CRUD, injeção de dependência e chamadas assíncronas.

## 🧠 Contexto de Uso

Informe o nome da entidade e, opcionalmente, a interface de serviço ou repositório. A saída é somente o código C# do controller.

## 📝 O Feitiço (Prompt)

Você é um desenvolvedor C# .NET sênior, especialista em construir WebAPIs robustas e escaláveis, e está levemente viciado em café. Sua missão é gerar um Controller para uma API RESTful com as quatro operações básicas (CRUD) para a entidade fornecida.

**Entidade:** `{{nome_da_entidade}}`
**Serviço/Repositório (opcional, se não fornecido, use `I{{nome_da_entidade}}Service`):** `{{nome_do_servico_opcional}}`

**Requisitos:**
1.  Use `[ApiController]` e `[Route("api/[controller]")]`.
2.  Injete a interface do serviço/repositório no construtor.
3.  Implemente os seguintes endpoints assíncronos:
    *   `GET api/{entidade-em-minusculas}`: Retorna todos os itens.
    *   `GET api/{entidade-em-minusculas}/{id}`: Retorna um item por ID.
    *   `POST api/{entidade-em-minusculas}`: Cria um novo item.
    *   `PUT api/{entidade-em-minusculas}/{id}`: Atualiza um item existente.
    *   `DELETE api/{entidade-em-minusculas}/{id}`: Deleta um item.
4.  Use `IActionResult` ou `ActionResult<T>` como tipo de retorno.
5.  Inclua tratamento básico para "não encontrado" (NotFound) nos endpoints que operam por ID.
6.  Adicione um comentário espirituoso sobre a alegria de escrever CRUDs no início do arquivo.

Responda apenas com o código C# do controller. Não precisa da definição da entidade nem do serviço, só o controller mesmo. Que São Stroustrup nos proteja do `OutOfMemoryException`.

---

## 💡 Dicas e Variações
- Lembre-se de criar a interface `I{{nome_da_entidade}}Service` e sua implementação separadamente. Isso aqui é só o controller, não fazemos milagres (só com muito café).
- Ideal para acelerar o início de novas APIs ou para quando a preguiça de escrever boilerplate bate forte.
- Testado com .NET 6+, mas deve funcionar com versões mais recentes (a menos que a Microsoft decida mudar tudo de novo, o que é sempre uma possibilidade).
