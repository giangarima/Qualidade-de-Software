# Projeto do aluno - Aula 11

## 1. Preparar o ambiente

```bash
python --version
python -m pip install -r requirements.txt
python -m pytest --version
python -m pytest -q
```

## 2. Exercício formativo

Implemente, usando TDD:

```python
calcular_taxa_entrega(distancia_km, total_pedido)
```

### Regras obrigatórias

1. Até 3 km, a taxa de entrega é R$ 5.
2. Acima de 3 km, acrescentar R$ 2 por quilômetro excedente.
3. Pedidos a partir de R$ 100 possuem entrega gratuita.

### Três cenários obrigatórios

- 2 km e pedido de R$ 50: taxa de R$ 5;
- 4 km e pedido de R$ 50: taxa de R$ 7;
- 5 km e pedido de R$ 100: taxa de R$ 0.

### Desafio opcional

- distância negativa deve gerar `ValueError`.

## 3. Processo esperado

Para cada comportamento:

1. escreva somente o teste desse comportamento;
2. execute e confirme a falha (Red);
3. implemente o mínimo necessário (Green);
4. execute toda a suíte;
5. passe ao próximo comportamento;
6. ao final, melhore a estrutura sem alterar o comportamento (Refactor).

Não implemente as três regras de uma vez.

## 4. Registro do ciclo

Use `REGISTRO_TDD.md` para registrar pelo menos um ciclo completo.