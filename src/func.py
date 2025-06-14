def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """
    Функция вычисляет стоимость товаров с учётом налога.
    prices -----
    tax_rate -----

    """

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


if __name__ == '__main__':
    calculate_taxes()