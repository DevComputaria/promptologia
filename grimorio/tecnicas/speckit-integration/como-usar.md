# 📖 Como usar o SpecKit com IAs

O segredo para um código perfeito gerado por IA não está no prompt, mas no **contexto**. Siga estes passos para o ritual completo:

## 1. Escolha o Pergaminho Correto
Vá até a pasta **[contextos/speckit/templates/](../../../contextos/speckit/templates/)** e escolha o template que melhor se adapta à sua necessidade (Funcionalidade, API ou Regra de Negócio).

## 2. Preencha a Especificação
Não poupe detalhes. Quanto mais preciso você for no preenchimento, menos a IA terá que "adivinhar" (e errar).

## 3. Realize a Invocação (Prompting)
Use um prompt estruturado que referencie explicitamente a especificação.

### Exemplo de Prompt de Invocação:
> "Atue como um Desenvolvedor Sênior. Abaixo, forneço uma especificação técnica seguindo o padrão SpecKit. Sua tarefa é implementar esta funcionalidade em [Linguagem/Framework], garantindo que todos os critérios de aceitação e restrições sejam respeitados.
>
> --- ESPECIFICAÇÃO ---
> [Cole o conteúdo do seu template preenchido aqui]
> -----------------------"

## 4. Refine o Resultado
Se a IA ignorar algum ponto, aponte diretamente para a seção da especificação que ela descumpriu. "Você esqueceu de tratar a restrição X descrita nas Tábuas da Regra de Negócio."
