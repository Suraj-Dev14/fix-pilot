from backend.app.tools.versions import compare_versions


result = compare_versions(
    service="product-service",
    old_version="v1.1.0",
    new_version="v1.2.0",
)

print(result)