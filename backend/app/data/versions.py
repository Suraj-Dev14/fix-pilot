VERSIONS = {
    "v1.1.0": {
        "service": "product-service",
        "code": """
def calculate_total(product):
    return product.get("price", 0)
""",
    },
    "v1.2.0": {
        "service": "product-service",
        "code": """
def calculate_total(product):
    return product["price"]
""",
    },
}