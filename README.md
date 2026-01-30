# devman-repo-template

Copier template for creating a new repository that stores **devenv** and **direnv** state under `./.devman/`,
so `devman run ...` can find and run your environment consistently.

## Requirements

- Copier
- direnv
- devenv
- devman (assumed installed as a `uv tool`)

## Usage

### With devman

```bash
devman new /path/to/this/template ./my-repo
```

### With copier directly

```bash
copier copy /path/to/this/template ./my-repo
```

## What gets generated

- `./.envrc` wired so devenv+direnv operate inside `./.devman/`
- `./.devman/devenv.nix` and `./.devman/devenv.yaml`
- `./justfile` convenience commands
- (Optional) minimal Python package with Typer CLI

## Updating

If you later tag releases of this template, consumers can run:

```bash
copier update
```
