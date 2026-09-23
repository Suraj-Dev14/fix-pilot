import os
import requests
from dotenv import load_dotenv
from .source import SourceProvider

load_dotenv()

class GitHubProvider(SourceProvider):
    """Source provider for GitHub repositories."""

    def __init__(self, repository: str):
        self.repository = repository
        self.token = os.getenv("GITHUB_TOKEN")

        if not self.token:
            raise ValueError("GITHUB_TOKEN environment variable not configured.")

    def _header(self) -> dict[str, str]:
        return {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_recent_commits(self, limit: int = 10) -> list[dict]:
        url = f"https://api.github.com/repos/{self.repository}/commits"

        response = requests.get(
            url,
            headers=self._header(),
            params={"per_page": limit},
            timeout=10,
        )

        response.raise_for_status()

        return [
            {
                "commit": item["sha"],
                "short_commit": item["sha"][:7],
                "message": item["commit"]["message"].splitlines()[0],
                "author": item["commit"]["author"]["name"],
            }
            for item in response.json()
        ]

    def compare_versions(
        self,
        old_version: str,
        new_version: str,
    ) -> dict:
        url = (
            f"https://api.github.com/repos/"
            f"{self.repository}/compare/{old_version}...{new_version}"
        )

        response = requests.get(
            url,
            headers=self._header(),
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        changed_files = []

        for file in data.get("files", []):
            changed_files.append(
                {
                    "filename": file["filename"],
                    "status": file["status"],
                    "additions": file["additions"],
                    "deletions": file["deletions"],
                    "changes": file["changes"],
                    "patch": file.get("patch"),
                }
            )

        return {
            "old_version": old_version,
            "new_version": new_version,
            "status": data.get("status"),
            "ahead_by": data.get("ahead_by"),
            "behind_by": data.get("behind_by"),
            "total_commits": data.get("total_commits"),
            "changed_files": changed_files,
        }