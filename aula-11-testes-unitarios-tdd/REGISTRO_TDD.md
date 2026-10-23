# Registro do ciclo de TDD

## Comportamento escolhido

Cobrar taxa de entrega fixa de R$ 5,00 para distância de até 3 km (2 km e pedido de R$ 50,00).

## Red

**Teste criado:** `test_ate_3km_cobra_taxa_fixa_de_5_reais`

**Motivo da falha:** a função `calcular_taxa_entrega` ainda não existia em `src/pedido.py`, então o pytest acusou `ImportError: cannot import name 'calcular_taxa_entrega'`.

## Green

**Implementação realizada:** criei a função retornando o valor fixo `5.0`, o mínimo para o teste passar. Os cenários seguintes foram feitos no mesmo formato: o de 4 km (R$ 7,00) falhou com `5.0 == 7.0` e passou ao adicionar o acréscimo de R$ 2,00 por km excedente. O de R$ 100,00 (R$ 0,00) falhou com `9.0 == 0.0` e passou ao adicionar a regra de entrega gratuita.

## Refactor

**Melhoria realizada:** troquei os números soltos (5, 3, 2 e 100) por constantes com nome (`TAXA_BASE`, `LIMITE_KM_TAXA_BASE`, `VALOR_POR_KM_EXCEDENTE`, `VALOR_MINIMO_ENTREGA_GRATIS`) e substituí o `if` do excedente por `max(0, distancia_km - LIMITE_KM_TAXA_BASE)`, sem alterar o comportamento.

**Resultado final:** os 7 testes da suíte passam (4 já existentes e os 3 novos).
