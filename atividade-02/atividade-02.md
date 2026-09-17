# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** 2026/2 - Noite

**Equipe:** Gian Garima

**Data:** 17/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Gian | [@giangarima] |


---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Os critérios para considerar uma funcionalidade "pronta" não estão claros. | Funcionalidades são entregues com entendimentos diferentes do que é suficiente, chegando aos usuários com defeitos que poderiam ter sido evitados. |
| Monopólio do teste | O profissional de QA se torna um gargalo no fluxo de desenvolvimento, atrasando as entregas, e os desenvolvedores deixam de se comprometer com a qualidade do próprio código. |
| Defeitos são identificados, mas nem sempre são registrados ou acompanhados. | Problemas conhecidos se perdem, voltam a aparecer, e a equipe perde visibilidade real da qualidade do produto, gerando retrabalho. |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. A qualidade é construída em todas as etapas do desenvolvimento, não apenas na fase de testes. O desenvolvedor influencia a qualidade ao escrever código limpo e testes unitários, o responsável pelo produto influencia ao definir critérios de aceitação claros e a liderança técnica influencia ao revisar decisões de arquitetura.

---

## 3. Tarefa 2: Papéis e competências

> Como a atividade foi realizada individualmente, um mesmo integrante analisou mais de um papel, de forma a viabilizar a matriz RACI da Tarefa 3.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Gian | Responsável pelo Produto (Product Owner) | Definir e validar os critérios de aceitação de cada funcionalidade, priorizar a correção de defeitos conforme o impacto no usuário e decidir, do ponto de vista de negócio, se uma versão está pronta para ser disponibilizada. | Conhecimento do domínio do negócio, capacidade de escrever critérios de aceitação testáveis, leitura básica de relatórios de teste e de defeitos. | Comunicação clara com o time, capacidade de priorização e tomada de decisão. |
| Gian | Desenvolvedor | Implementar a funcionalidade, escrever e manter testes unitários, e corrigir defeitos atribuídos a ele. | Domínio da linguagem utilizados no LocalEats, boas práticas de código limpo e de revisão de código. | Responsabilidade pela própria entrega, abertura a feedback e pensamento crítico sobre casos de borda. |
| Gian | QA | Planejar e executar testes do sistema (funcionais e exploratórios), registrar e acompanhar defeitos até o fechamento e contribuir na revisão dos critérios de aceitação | Técnicas de teste e uso de ferramentas de rastreamento de defeitos. | Atenção a detalhes, pensamento crítico, comunicação objetiva ao reportar defeitos e colaboração com os desenvolvedores. |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizem:
- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Responsável pelo Produto | Desenvolvedor | QA |
|---|:---:|:---:|:---:|
| Definir critérios de aceitação | R, A | C | C |
| Revisar requisitos | A | C | R |
| Implementar a funcionalidade | I | R, A | C |
| Revisar o código | I | R, A | C |
| Criar testes unitários | I | R, A | I |
| Planejar e executar testes do sistema | C | C | R, A |
| Registrar e acompanhar defeitos | I | R | R, A |
| Priorizar a correção dos defeitos | R, A | I | C |
| Aprovar a disponibilização da versão | R, A | I | C |

### 4.1 Lacuna ou conflito encontrado

**Atividades concentradas:**
"Registrar e acompanhar defeitos" e "Planejar e executar testes do sistema". 
Se o QA concentrar sozinho a execução (R) e a responsabilidade (A) de todos os testes de sistema e registros de defeito, ele continuará operando na abordagem tradicional (cascata). Isso gera o gargalo onde o código fica parado esperando a aprovação de uma única pessoa, ferindo a prática da distribuição de tarefas de validação.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definir uma Definição de Pronto compartilhada e visível pela equipe, incluindo critérios de aceitação atendidos, testes unitários passando e revisão de código aprovada. | Os critérios para considerar uma funcionalidade "pronta" não estão claros. | Product Owner, Desenvolvedor, QA. |
| Adotar um quadro/ferramenta de rastreamento de defeitos com campos obrigatórios de responsável e status, revisado em reuniões periódicas de acompanhamento. | Defeitos são identificados, mas nem sempre são registrados ou acompanhados. | QA, Desenvolvedor, Product Owner. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
Gemini (Google)

**Como foi utilizada:**
Apoio para estruturar o documento no formato Markdown e organizar visualmente as tabelas, especialmente a Matriz RACI e os Papéis de QA.

**Como as respostas foram verificadas:**
Cruzei cada problema, papel e atribuição da Matriz RACI com os cenários descritos no enunciado. Confirmei que as soluções propostas resolvem diretamente as falhas relatadas (como a falta de clareza na aprovação de versões e o gargalo de testes no QA).