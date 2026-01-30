{% if include_python -%}
from typer.testing import CliRunner

from {{ package_name }}.cli import app

runner = CliRunner()


def test_hello() -> None:
    result = runner.invoke(app, ["hello", "World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout
{%- else -%}
def test_placeholder() -> None:
    # include_python=false
    assert True
{%- endif %}
