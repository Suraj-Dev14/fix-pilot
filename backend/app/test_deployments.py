from backend.app.tools.deployments import get_deployment_history


results = get_deployment_history(
    service="product-service",
)

print(results)