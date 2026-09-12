from backend.app.tools.api import inspect_api_response


result = inspect_api_response(
    service="product-service",
)

print(result)