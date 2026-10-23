"""Regras de negocio relacionadas ao calculo de pedidos."""


def validar_item(item: dict) -> None:
    """Valida preco e quantidade de um item.

    Raises:
        ValueError: se o preco ou a quantidade nao forem positivos.
    """
    if item["preco"] <= 0:
        raise ValueError("O preco deve ser positivo.")

    if item["quantidade"] <= 0:
        raise ValueError("A quantidade deve ser positiva.")


def calcular_total(itens: list[dict]) -> float:
    """Calcula o total do pedido.

    Uma lista vazia resulta em total igual a zero.
    """
    total = 0

    for item in itens:
        validar_item(item)
        total += item["preco"] * item["quantidade"]

    return total


TAXA_BASE = 5.0
LIMITE_KM_TAXA_BASE = 3
VALOR_POR_KM_EXCEDENTE = 2.0
VALOR_MINIMO_ENTREGA_GRATIS = 100.0


def calcular_taxa_entrega(distancia_km, total_pedido):
    """Calcula a taxa de entrega.

    Regras:
    - ate 3 km, a taxa e R$ 5;
    - acima de 3 km, acrescenta R$ 2 por quilometro excedente;
    - pedidos a partir de R$ 100 possuem entrega gratuita.
    """
    if total_pedido >= VALOR_MINIMO_ENTREGA_GRATIS:
        return 0.0

    km_excedentes = max(0, distancia_km - LIMITE_KM_TAXA_BASE)
    return TAXA_BASE + km_excedentes * VALOR_POR_KM_EXCEDENTE
