# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** 2026/2 - Noite

**Equipe:** Gian Garima

**Data:** 18/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Gian | [@giangarima] |

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se a funcionalidade de busca do LocalEats retorna corretamente os restaurantes que correspondem ao termo digitado pelo usuário.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Gian | Pesquisar restaurantes por especialidade ou localização | Se o campo de busca por texto retorna corretamente restaurantes existentes ao buscar pelo nome do restaurante ou por uma culinária já reconhecida pelo sistema, e se retorna a mensagem correta quando o termo não existe. |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Fazer pedido | Depende de um fluxo de checkout separado. |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Sistema | O fluxo de busca será analisado de ponta a ponta pela interface, sem acesso ao código-fonte. |
| Tipos de teste | Funcional | O objetivo é verificar se a busca retorna o resultado correto. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Serão consideradas apenas as entradas digitadas e os resultados exibidos na tela, sem análise do código de busca. |
| Técnicas de teste | Particionamento de equivalência | A entrada do campo de busca pode ser dividida em classes (termo válido existente, termo inválido/inexistente) que devem, teoricamente, produzir comportamentos diferentes e observáveis. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Aplicação LocalEats (<https://local-eats-unisenac.vercel.app/>), navegador atualizado, uma conta de teste já cadastrada e pelo menos um restaurante conhecido (nome e culinária) disponível na base para servir de referência. |
| Responsáveis pelo planejamento | Gian |
| Responsáveis pela especificação dos casos | Gian |
| Responsáveis pela futura execução | Gian |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Aplicação disponível, usuário autenticado e existência de pelo menos um restaurante cadastrado com nome e culinária conhecidos. |
| Saída | Os três casos de teste planejados executados e os resultados observados registrados. |
| Suspensão | Aplicação indisponível ou impossibilidade de autenticação no sistema durante a execução. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|---|---|---|---|
| R01 | Gian | Pesquisar restaurantes por especialidade ou localização | O campo de busca por texto não localizar um restaurante existente ao buscar pelo seu nome. | Usuários acreditam que o restaurante não existe, perdendo confiança na aplicação e deixando de concluir pedidos. | Alta | Alto | Alta | Comportamento já observado em exploração anterior: buscar pelo nome de um restaurante cadastrado e favoritado retornou "Nenhum restaurante encontrado". |
| R02 | Gian | Pesquisar restaurantes por especialidade ou localização | O campo de busca por texto não localizar restaurantes ao buscar por um termo de culinária válido (ex.: "Brasileira"), mesmo esse termo estando disponível como botão de filtro na mesma tela. | Usuários deixam de encontrar restaurantes de uma culinária que realmente existe na base, reduzindo a percepção de variedade e prejudicando a experiência de busca. | Alta | Alto | Alta | Comportamento já observado em exploração anterior: buscar "Brasileira" no campo de texto retornou "Nenhum restaurante encontrado", mesmo esse termo sendo reconhecido pelos botões de filtro da própria tela. |

### 3.2 Aplicação das técnicas

#### Análise do integrante 1

**Integrante:** Gian

**Funcionalidade:** Pesquisar restaurantes por especialidade 
ou localização

**Risco relacionado:** R01 e R02

**Técnica escolhida:** Particionamento de equivalência

**Por que a técnica foi escolhida:**
A entrada do campo de busca pode ser agrupada em classes que deveriam produzir resultados diferentes: termos que correspondem a algo existente no sistema (nome de restaurante ou culinária) e termos que não correspondem a nada. Comparar o comportamento observado entre essas classes ajuda a evidenciar se a falha de busca afeta toda e qualquer entrada de texto, ou apenas alguns casos específicos.

**Aplicação da técnica:**

| Classe | Situação | Valor representativo |
|---|---|---|
| Válida | Nome de um restaurante existente digitado exatamente | "Restaurante Sabor 0" |
| Válida | Termo de culinária existente, igual ao rótulo do botão de filtro | "Brasileira" |
| Inválida | Termo que não corresponde a nenhum restaurante, culinária ou localização cadastrada | "xyzinexistente123" |

**Casos derivados:** CT01, CT02 e CT03

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Buscar restaurante existente pelo nome

**Integrante responsável:** Gian

**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização

**Risco ou requisito relacionado:** R01

**Técnica utilizada:** Particionamento de equivalência (classe válida — nome existente)

**Pré-condição:**
Usuário autenticado e existir um restaurante cadastrado com o nome "Restaurante Sabor 0".

**Dados de entrada:**
Termo de busca: "Restaurante Sabor 0"

**Passos:**

1. Acessar a tela "Explorar".
2. Digitar "Restaurante Sabor 0" no campo de busca.
3. Clicar em "Buscar".

**Resultado esperado:**
O sistema exibe o "Restaurante Sabor 0" na lista de resultados.

---

### CT02: Buscar por culinária existente já usada como filtro

**Integrante responsável:** Gian
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização
**Risco ou requisito relacionado:** R02
**Técnica utilizada:** Particionamento de equivalência (classe válida — culinária existente)

**Pré-condição:**
Usuário autenticado, existir pelo menos um restaurante cadastrado com a culinária "Brasileira", disponível também como botão de filtro na tela "Explorar".

**Dados de entrada:**
Termo de busca: "Brasileira"

**Passos:**

1. Acessar a tela "Explorar".
2. Digitar "Brasileira" no campo de busca.
3. Clicar em "Buscar".

**Resultado esperado:**
O sistema exibe os restaurantes cadastrados com a culinária "Brasileira".

---

### CT03: Buscar termo inexistente (controle negativo)

**Integrante responsável:** Gian
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização
**Risco ou requisito relacionado:** R01 e R02 (usado como comparação entre a classe inválida e as classes válidas testadas em CT01 e CT02)
**Técnica utilizada:** Particionamento de equivalência (classe inválida)

**Pré-condição:**
Usuário autenticado.

**Dados de entrada:**
Termo de busca: "xyzinexistente123"

**Passos:**

1. Acessar a tela "Explorar".
2. Digitar "xyzinexistente123" no campo de busca.
3. Clicar em "Buscar".

**Resultado esperado:**
O sistema exibe a mensagem "Nenhum restaurante encontrado".

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Gian | Pesquisar restaurantes por especialidade ou localização | R01 | Particionamento de equivalência | CT01 e CT03 |
| Gian | Pesquisar restaurantes por especialidade ou localização | R02 | Particionamento de equivalência | CT02 e CT03 |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
Claude (Anthropic)

**Como foi utilizada:**
Auxílio na formatação do documento em Markdown e no refinamento da redação técnica, garantindo clareza na formulação do Plano de Testes, na escrita dos Casos de Teste e na estruturação correta da Matriz de Rastreabilidade.

**Uma sugestão que precisou ser alterada ou rejeitada:**
A ferramenta havia sugerido inicialmente aplicar a técnica de tabela de decisão para a funcionalidade de busca. Rejeitei essa sugestão porque a busca não depende da combinação de múltiplas condições lógicas simultâneas (como ocorre no fluxo de fechamento de pedido, com autenticação + itens no carrinho), e sim de testar o comportamento de um mesmo campo de texto diante de grupos diferentes de informações. Por isso, optei pelo particionamento de equivalência, que é a técnica correta para esse cenário.

**Como as respostas foram verificadas:**
Conferi cada risco e caso de teste comparando com o comportamento real já documentado durante a exploração da Atividade 1 (onde buscas por nome e por culinária retornaram a falha "Nenhum restaurante encontrado"). Isso garantiu que os casos de teste criados não fossem genéricos.