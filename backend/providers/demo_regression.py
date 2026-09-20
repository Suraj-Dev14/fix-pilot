from backend.app.data.product_logic import calculate_total_v1_2

from .regression import RegressionProvider


class DemoRegressionProvider(RegressionProvider):
  def run(self, command: str | None = None) -> dict:
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