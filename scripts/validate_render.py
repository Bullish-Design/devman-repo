from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from copier import run_copy


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]

    with tempfile.TemporaryDirectory() as td:
        dst = Path(td) / "sample"
        run_copy(
            src_path=str(repo_root),
            dst_path=str(dst),
            data={
                "project_name": "Sample Devman Repo",
                "project_slug": "sample-devman-repo",
                "package_name": "sample_devman_repo",
                "description": "Sample render for CI",
                "author_name": "CI",
                "include_python": True,
                "python_version": "3.13",
                "license": "MIT",
            },
            unsafe=True,
        )

        # Basic structure checks
        assert (dst / ".envrc").exists()
        assert (dst / ".devman" / "devenv.nix").exists()
        assert (dst / ".devman" / "devenv.yaml").exists()
        assert (dst / "justfile").exists()
        assert (dst / "pyproject.toml").exists()
        assert (dst / "src" / "sample_devman_repo" / "cli.py").exists()

        # Python syntax checks
        subprocess.check_call(["python", "-m", "compileall", str(dst / "src")])

    print("OK")


if __name__ == "__main__":
    main()
