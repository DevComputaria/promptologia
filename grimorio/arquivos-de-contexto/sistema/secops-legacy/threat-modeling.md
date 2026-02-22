# 🛡️ Threat Modeling Automatizado com LLM

**Categoria:** secops
**Objetivo:** Gerar um modelo preliminar de ameaças (Threat Model) com base em um cenário técnico, incluindo possíveis vetores de ataque, ativos expostos, impactos e controles de mitigação.
**Input esperado:** Uma descrição textual contendo arquitetura resumida, tecnologias utilizadas, fluxos de dados e contexto operacional (ex: "API pública com autenticação JWT acessando banco PostgreSQL via VPC privada").
**Saída esperada:** Estrutura completa de Threat Modeling com as seguintes seções:

- Identificação de Ativos
- Atores (internos/externos)
- Superfícies de Ataque
- Ameaças potenciais por categoria (base STRIDE)
- Técnicas MITRE ATT&CK relacionadas
- Controles de mitigação (com base em OWASP e NIST)
- Sugestão de priorização com base em impacto e facilidade de exploração

---

## 🔮 Prompt

Você é um analista de segurança sênior com experiência em modelagem de ameaças, DevSecOps e compliance regulatório.

Sua tarefa é analisar o seguinte cenário técnico e gerar um **modelo de ameaças completo**, considerando os padrões STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), MITRE ATT&CK e práticas do OWASP.

Utilize a seguinte estrutura para a resposta:

---

## 🧩 1. Identificação de Ativos

Liste os ativos técnicos e lógicos que devem ser protegidos. Ex: APIs, banco de dados, tokens, sessões, pipelines de CI/CD.

## 👥 2. Atores Envolvidos

Classifique os atores (usuários, sistemas, atacantes) como internos ou externos e descreva seu nível de acesso.

## 🔓 3. Superfícies de Ataque

Liste os pontos de entrada ou interação que podem ser explorados (ex: endpoints públicos, callbacks, arquivos, autenticação externa, exposed secrets).

## ⚠️ 4. Ameaças por Categoria (STRIDE)

Crie uma tabela com os riscos identificados usando o modelo STRIDE:

| Categoria | Descrição da Ameaça | Ativo Afetado | Vetor de Exploração |
|-----------|---------------------|---------------|----------------------|

## 🎯 5. Técnicas MITRE ATT&CK Associadas

Associe técnicas reais do framework MITRE ATT&CK relevantes às ameaças detectadas.

## 🔐 6. Controles de Mitigação

Sugira contramedidas, incluindo práticas como validação de entrada, hardening de autenticação, logging estruturado, WAF, segmentação de rede, uso de IAM, etc.

## 📊 7. Priorização

Classifique as ameaças em alta, média ou baixa prioridade com base em:

- Potencial de impacto (negócio, reputação, confidencialidade)
- Facilidade de exploração (scripts conhecidos, APIs expostas, falta de autenticação)
- Probabilidade baseada em exposição real

---

### 📥 Cenário fornecido:

{{CENARIO_AQUI}}

---

## 🧠 Notas

- Use vocabulário técnico, mas objetivo.
- Traga referências cruzadas com OWASP Top 10 e MITRE ATT&CK se possível.
- A resposta deve servir como base para criação de uma planilha de riscos ou uma threat board no Jira.
---

✅ Exemplos de uso no repositório

Você poderá incluir esse prompt em situações como:

Análise de risco de um novo microserviço

CI/CD pipelines que envolvem segredos e chaves

Auditoria de APIs públicas ou exposição a parceiros externos

Modelagem de ameaças para processos de compliance PCI, ISO, LGPD
