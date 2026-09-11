from backend.app.tools.logs import search_logs


results = search_logs(
    service="product-service",
    search_term="KeyError",
)

print(results)