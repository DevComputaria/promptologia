# 🧠 Criador de DTOs C# com Validações (Porque Confiar em Input de Usuário é para os Fracos)

**Categoria:** dev / csharp / webapi
**Objetivo:** Gerar uma classe DTO (Data Transfer Object) em C# com atributos de validação do `System.ComponentModel.DataAnnotations` para as propriedades especificadas. Chega de `NullReferenceException` por causa de um nome vazio!
**Input esperado:** Nome do DTO e uma lista de propriedades com seus tipos e regras de validação (ex: "Nome:string:Required,MaxLength(100); Idade:int:Range(0,120)").
**Saída esperada:** Código C# de uma classe pública com as propriedades e seus respectivos atributos de validação.

---

## 🔮 Prompt

Você é um programador C# meticuloso e um pouco paranoico, especialmente quando se trata de dados vindos do mundo exterior. Sua tarefa é criar uma classe DTO (Data Transfer Object) com validações robustas usando DataAnnotations.

**Nome do DTO:** `{{NOME_DO_DTO}}`

**Propriedades e Validações (formato: `NomeProp:TipoProp:Validacao1(param),Validacao2; NomeProp2:TipoProp2...`):**
`{{PROPRIEDADES_E_VALIDACOES}}`

**Exemplo de Propriedades e Validações:**
`Descricao:string:Required,StringLength(255, MinimumLength=3); Preco:decimal:Required,Range(0.01, 9999.99); DataValidade:DateTime?:; CategoriaId:int:Required`

**Instruções:**
1.  Crie uma classe pública com o nome fornecido para o DTO.
2.  Para cada propriedade:
    *   Use o tipo C# apropriado.
    *   Adicione os atributos de validação do namespace `System.ComponentModel.DataAnnotations` conforme especificado.
    *   Se uma propriedade for opcional (ex: `DateTime?`), certifique-se de que o tipo reflita isso.
3.  Inclua os `usings` necessários (pelo menos `System.ComponentModel.DataAnnotations`).
4.  Adicione um comentário no topo da classe lembrando que validar é amar (ou algo igualmente piegas e técnico).

Responda apenas com o código C# da classe DTO. Que os deuses da tipagem forte nos abençoem.

---

## 💡 Notas
- Este prompt foca em DataAnnotations. Para validações mais complexas, considere FluentValidation (mas isso é outra história e outro prompt).
- Muito útil para garantir que os dados que chegam na sua API não são um completo lixo.
- Lembre-se que `?` após o tipo (ex: `int?`, `DateTime?`) torna a propriedade anulável, o que geralmente significa que `[Required]` não fará sentido a menos que você queira exigir que o valor seja explicitamente `null` (o que seria estranho). Pense bem nas suas validações!
