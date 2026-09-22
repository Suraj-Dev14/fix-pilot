from pathlib import Path
import subprocess

from .source import SourceProvider


class LocalGitProvider(SourceProvider):
    """Source provider backed by a local Git repository."""

    def get_recent_commits(self, limit: int = 10) -> list[dict]:
        """Return recent commits from the local repository."""

        output = self._run_git(
            "log",
            f"-{limit}",
            "--pretty=format:%H|%h|%s",
        )

        commits = []

        for line in output.splitlines():
            if not line:
                continue

            full_sha, short_sha, message = line.split("|", 2)

            commits.append(
                {
                    "commit": full_sha,
                    "short_commit": short_sha,
                    "message": message,
                }
            )

        return commits

    def __init__(self, repository_path: str):
        self.repository_path = Path(repository_path).resolve()

        if not self.repository_path.exists():
            raise ValueError(
                f"Repository path does not exist: {self.repository_path}"
            )

    def compare_versions(
        self,
        old_version: str,
        new_version: str,
    ) -> dict:
        old_commit = self._resolve_commit(old_version)
        new_commit = self._resolve_commit(new_version)

        diff = self._run_git(
            "diff",
            "--no-ext-diff",
            old_commit,
            new_commit,
        )

        changed_files = self._run_git(
            "diff",
            "--name-only",
            old_commit,
            new_commit,
        )

        return {
            "old_version": old_version,
            "new_version": new_version,
            "old_commit": old_commit,
            "new_commit": new_commit,
            "changed_files": [
                file
                for file in changed_files.splitlines()
                if file
            ],
            "diff": diff,
        }

    def _resolve_commit(self, revision: str) -> str:
        return self._run_git(
            "rev-parse",
            revision,
        ).strip()

    def _run_git(self, *args: str) -> str:
        try:
            result = subprocess.run(
                ["git", *args],
                cwd=self.repository_path,
                capture_output=True,
                text=True,
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(
                f"Git command failed: git {' '.join(args)}\n"
                f"{exc.stderr.strip()}"
            ) from exc

        return result.stdout