import pytest
from src.pedido import calcular_taxa_entrega, calcular_total

def test_calcula_total_de_varios_itens():
    itens = [
        {"preco": 20, "quantidade": 2},
        {"preco": 10, "quantidade": 1},
    ]

    total = calcular_total(itens)
    assert total == 50


def test_retorna_zero_quando_lista_esta_vazia():
    itens = []
    total = calcular_total(itens)

    assert total == 0


def test_rejeita_item_com_preco_zero():
    itens = [{"preco": 0, "quantidade": 1}]

    with pytest.raises(ValueError, match="preco"):
        calcular_total(itens)


def test_rejeita_item_com_quantidade_zero():
    itens = [{"preco": 20, "quantidade": 0}]

    with pytest.raises(ValueError, match="quantidade"):
        calcular_total(itens)


def test_ate_3km_cobra_taxa_fixa_de_5_reais():
    assert calcular_taxa_entrega(2, 50) == 5.0


def test_acima_de_3km_cobra_2_reais_por_km_excedente():
    assert calcular_taxa_entrega(4, 50) == 7.0


def test_pedido_a_partir_de_100_reais_tem_entrega_gratuita():
    assert calcular_taxa_entrega(5, 100) == 0.0
