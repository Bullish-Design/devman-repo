{% if include_python -%}
from __future__ import annotations

import typer

app = typer.Typer(add_completion=False)


@app.command()
def hello(name: str) -> None:
    """Say hello."""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
{%- else -%}
# Python scaffold disabled (include_python=false).
# Delete this file if you don't want Python in this repository.
{%- endif %}
