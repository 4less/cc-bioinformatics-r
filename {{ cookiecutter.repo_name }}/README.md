# cc-bioinformatics-r

Cookiecutter template for bioinformatics (analysis) projects with R as a main driver. Inspired by https://github.com/maxplanck-ie/cookiecutter-bioinformatics-project/ but I am not a fan of thousand folders in the base directory, so the template keeps a broad split into code, data, and results. Workflows are driven with `just` instead of a Makefile.

## Layout

```
code/
├─ src/              — R source, scripts, workflows, notebooks, tests
├─ scripts/
├─ workflows/
├─ notebooks/
data/                — raw/external/interim inputs (usually gitignored)
├─ external/
├─ interim/
├─ raw/
notes/               — free-form notes
results/             — analysis outputs, figures, reports (gitignored)
├─ publication/
├─ general/
sandbox/             — scratch space for quick experiments
├─ src/
├─ data/
```

## Quickstart

1. Install R (≥ 4.2 recommended) and `just` (https://github.com/casey/just).
2. Install renv if needed: `R -e "install.packages('renv')"`.
3. From the project root: `just setup` to install/restore R packages. It also snapshots explicitly so the lockfile stays in sync.
4. Add packages with `R -e "renv::install('pkg')"`, then `just snapshot` to record them (snapshot is explicit, so it captures everything installed in the project library).
5. Run your own recipes via `just` (see the `justfile` for examples).

## Task runner (`just`)

Core recipes are defined in `justfile`:

- `just setup` — install `renv` if missing and restore packages from `renv.lock`.
- `just restore` — restore the locked environment without reinstalling `renv`.
- `just snapshot` — write the current library state to `renv.lock`.
- `just clean-renv` — drop the local renv library and lockfile (fresh start).
- Add your own workflow commands (e.g., `just run-pipeline`) as needed.
