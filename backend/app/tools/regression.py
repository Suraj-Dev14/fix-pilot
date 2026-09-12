from strands import tool

from backend.app.data.product_logic import calculate_total_v1_2


@tool
def run_regression_test() -> dict:
    """Run a regression test for the missing price incident."""

    product_without_price = {
        "id": "product-101",
        "name": "Wireless Headphones",
    }

    try:
        result = calculate_total_v1_2(product_without_price)

        return {
            "passed": True,
            "result": result,
        }

    except Exception as error:
        return {
            "passed": False,
            "error_type": type(error).__name__,
            "error": str(error),
        }