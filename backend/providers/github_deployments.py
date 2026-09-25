import os
from dotenv import load_dotenv

load_dotenv()

import requests

from .deployments import DeploymentProvider


class GitHubDeploymentProvider(DeploymentProvider):
    """Deployment provider backed by GitHub Deployments."""

    def __init__(self, repository: str):
        self.repository = repository
        self.token = os.getenv("GITHUB_TOKEN")

        if not self.token:
            raise ValueError(
                "GITHUB_TOKEN environment variable is not configured."
            )

    def _headers(self) -> dict[str, str]:
        return {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_history(self, service: str) -> list[dict]:
        deployments = []
        page = 1

        while True:
            url = (
                f"https://api.github.com/repos/"
                f"{self.repository}/deployments"
            )

            response = requests.get(
                url,
                headers=self._headers(),
                params={
                    "per_page": 30,
                    "page": page,
                },
                timeout=10,
            )

            response.raise_for_status()

            page_deployments = response.json()

            if not page_deployments:
                break

            for deployment in page_deployments:
                deployment_id = deployment["id"]

                deployments.append(
                    {
                        "service": service,
                        "deployment_id": deployment_id,
                        "sha": deployment["sha"],
                        "ref": deployment["ref"],
                        "environment": deployment.get("environment"),
                        "status": self._get_deployment_status(
                            deployment_id
                        ),
                        "created_at": deployment.get("created_at"),
                        "updated_at": deployment.get("updated_at"),
                        "creator": (
                            deployment.get("creator") or {}
                        ).get("login"),
                    }
                )

            if len(page_deployments) < 30:
                break

            page += 1

        return deployments


    def _get_deployment_status(self, deployment_id: int) -> str | None:
        url = (
            f"https://api.github.com/repos/"
            f"{self.repository}/deployments/{deployment_id}/statuses"
        )

        response = requests.get(
            url,
            headers=self._headers(),
            params={"per_page": 1},
            timeout=10,
        )

        response.raise_for_status()

        statuses = response.json()

        if not statuses:
            return None

        return statuses[0].get("state")