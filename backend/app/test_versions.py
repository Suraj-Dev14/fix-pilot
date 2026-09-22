from backend.app.tools.versions import compare_versions


result = compare_versions(
    old_version="43cc9a6",
    new_version="d6eb0e9",
)

print(result)