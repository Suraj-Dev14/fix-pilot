def calculate_total_v1_1(product: dict) -> int:
    return product.get("price", 0)


def calculate_total_v1_2(product: dict) -> int:
    return product["price"]