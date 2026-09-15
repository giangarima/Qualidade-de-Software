# Atividade 01: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** 2026/2 - Noite

**Equipe:** Gian Garima

**Data:** 15/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Gian | [@giangarima] |

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Poder pesquisar restaurantes por especialidade ou localização. | Usuário final | O usuário não consegue filtrar as opções que o interessa e precisará navegar por todo o site, prejudicando sua experiência de uso. |
| Explícita | Poder criar uma conta e entrar no sistema para realizar pedidos. | Usuário final / Negócio | Sem autenticação, o usuário não consegue realizar pedidos, o que inviabiliza o modelo de negócio do aplicativo. |
| Implícita | A busca deve retornar resultados coerentes com o que o usuário digita, mesmo quando o termo digitado corresponde a um valor já existente no sistema (como uma culinária ou o nome de um restaurante). | Usuário final | O usuário pode acreditar que não há restaurantes disponíveis (mesmo existindo), abandonando a busca e perdendo a confiança na aplicação. |
| Implícita | As informações exibidas (status de pedido, valores e restaurantes favoritados) devem ser consistentes e estar atualizadas. | Usuário final / Negócio | Informações inconsistentes (ex: pedido preso em "pendente" por muito tempo) geram desconfiança e podem levar à desistência do uso do aplicativo. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim. O LocalEats, por exemplo, implementa a funcionalidade de busca, atendendo ao requisito explícito, mas isso não garante qualidade se a necessidade implícita de obter resultados coerentes não for atendida. Durante a exploração, buscar tanto pelo nome de um restaurante cadastrado quanto por um termo de culinária existente (ex: "Brasileira") retornou "Nenhum restaurante encontrado". A funcionalidade "existe", mas não atende à expectativa do usuário.

---

## 3. Tarefa 2: Exploração da aplicação

> Cada integrante deve explorar uma funcionalidade, realizando uma utilização esperada e uma utilização alternativa, inválida ou incompleta. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Gian | Pesquisar restaurantes por especialidade ou localização | Uso esperado: utilizei os botões de filtro de categoria ("Todos", "Brasileira", etc.) na tela Explorar, com dado válido. Uso alternativo/inválido (1): digitei o nome de um restaurante já existente e favoritado, "Restaurante Sabor 0", no campo de texto de busca. Uso alternativo/inválido (2): digitei no mesmo campo de texto o termo "Brasileira", que é uma culinária válida e já exibida como opção de filtro na própria tela. | No uso esperado (botões de filtro), os restaurantes foram listados normalmente por categoria. Nos dois usos alternativos, o campo de texto de busca retornou "Nenhum restaurante encontrado", tanto para o nome do restaurante quanto para o termo de culinária "Brasileira", mesmo esse termo sendo uma opção válida disponível como botão de filtro na mesma tela. Isso indica que o campo de busca por texto não está funcionando corretamente para nenhum dos critérios testados, apenas os botões de filtro de categoria funcionam. | [ver evidência](evidencias/busca-restaurante-sabor-0-nao-encontrado.png), [ver evidência](evidencias/exploracao-favoritos-restaurante-sabor-0.png) e [ver evidência](evidencias/busca-brasileira-nao-encontrada.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

> Cada integrante deve formular um requisito de qualidade relacionado à mesma funcionalidade explorada na Tarefa 2. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Gian | O campo de busca por texto deve retornar resultados corretos tanto para nomes de restaurantes quanto para termos de culinária/localização já reconhecidos pelo próprio sistema (os mesmos usados nos botões de filtro), e não apenas quando o usuário utiliza os botões de categoria. | Adequação Funcional — Corretude Funcional (ISO/IEC 25010) | A busca por texto não é apenas incompleta (faltando cobrir um critério): ela apresenta um resultado incorreto mesmo para um termo que o próprio sistema reconhece e disponibiliza como botão de filtro ("Brasileira"). Isso caracteriza uma falha de corretude funcional, já que o sistema não fornece o resultado correto com a precisão esperada para uma entrada válida. | Selecionar uma amostra de termos válidos já usados no sistema (nomes de restaurantes cadastrados e todas as culinárias exibidas nos botões de filtro) e digitá-los, um a um, no campo de busca por texto, comparando o resultado obtido com o resultado esperado (o mesmo que o botão de filtro equivalente retorna). |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
Gemini (Google)

**Como foi utilizada:**
Apoio para estruturar o documento no formato Markdown, discutir a norma ISO/IEC 25000 (25010) para encontrar a subcaracterística adequada (Adequação Funcional/Corretude Funcional para o defeito da barra de pesquisa) e refinar a redação técnica das necessidades implícitas e explícitas.

**Como as respostas foram verificadas:**
As respostas foram validadas conferindo as exigências do enunciado da atividade e checando os conceitos de qualidade de software para garantir que a subcaracterística escolhida se aplicava perfeitamente ao defeito funcional testado.