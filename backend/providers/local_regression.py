import shlex
import subprocess

from .regression import RegressionProvider


class LocalRegressionProvider(RegressionProvider):
    """Regression provider that runs a configured local test command."""

    def __init__(self, command: str):
        if not command.strip():
            raise ValueError("Regression command cannot be empty.")

        self.command = command

    def run(self, command: str | None = None) -> dict:
        """Run the configured regression command."""

        selected_command = command or self.command

        try:
            result = subprocess.run(
                shlex.split(selected_command),
                capture_output=True,
                text=True,
                check=False,
            )

        except OSError as exc:
            return {
                "passed": False,
                "error_type": type(exc).__name__,
                "error": str(exc),
            }

        return {
            "passed": result.returncode == 0,
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "command": selected_command,
        }