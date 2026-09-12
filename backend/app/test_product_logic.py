from backend.app.data.product_logic import (
    calculate_total_v1_1,
    calculate_total_v1_2,
)


product_without_price = {
    "id": "product-101",
    "name": "Wireless Headphones",
}


print("v1.1.0 result:")
print(calculate_total_v1_1(product_without_price))


print("v1.2.0 result:")
print(calculate_total_v1_2(product_without_price))