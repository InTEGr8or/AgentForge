import os
import subprocess
import sys
from typing import Optional


def run_command(command: str, cwd: Optional[str] = None) -> None:
    """Executes a shell command and prints its output."""
    print(f"Executing: {command} in {cwd if cwd else os.getcwd()}")
    try:
        result = subprocess.run(
            command, shell=True, check=True, cwd=cwd, capture_output=True, text=True
        )
        print(result.stdout)
        if result.stderr:
            print(f"Error Output:\n{result.stderr}", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}", file=sys.stderr)
        print(f"Stdout:\n{e.stdout}", file=sys.stderr)
        print(f"Stderr:\n{e.stderr}", file=sys.stderr)
        sys.exit(e.returncode)


def deploy_cdk() -> None:
    iac_dir = "."  # Now at root
    venv_path = os.path.join(iac_dir, ".venv")

    # Ensure uv virtual environment exists
    print("Ensuring uv virtual environment exists...")
    run_command(f"uv venv {venv_path}")

    # Install dependencies using uv
    print("Installing dependencies with uv...")
    run_command(
        f"uv pip install {iac_dir} --python {os.path.join(venv_path, 'bin', 'python')}"
    )
    run_command(
        f"uv pip install -r {os.path.join(iac_dir, 'requirements-dev.txt')} --python {os.path.join(venv_path, 'bin', 'python')}"
    )

    # Run cdk deploy from within the iac directory
    print("Running cdk deploy...")
    run_command("cdk deploy", cwd=iac_dir)


if __name__ == "__main__":
    deploy_cdk()
