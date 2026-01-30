\
{ pkgs, config, ... }:

let
  root = config.git.root;
in
{
  packages = with pkgs; [
    git
    just
    jq
    ripgrep
  ];

  languages.python = {
    enable = true;
    version = "{{ python_version }}";
    directory = "../";
    venv.enable = true;
    uv.enable = true;
  };

  # Keep stable command interfaces here; wrap developer workflows in justfile.
  scripts.test.exec = ''
    cd "${root}"
    {% if include_python -%}
    python -m pytest
    {%- else -%}
    echo "No Python scaffold selected; add your own tests."
    {%- endif %}
  '';

  scripts.hello.exec = ''
    cd "${root}"
    {% if include_python -%}
    python -m {{ package_name }}.cli hello "$@"
    {%- else -%}
    echo "No Python scaffold selected."
    {%- endif %}
  '';
}
