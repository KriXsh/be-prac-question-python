# be-prac-question-python

Personal practice repo for **Python fundamentals** (lecture-wise) and **DSA problems** (topic-wise).
Every practice file holds the solution and its `test_*` functions together, so one `pytest`
run checks everything.

## Layout

```
be-prac-question-python/
├── lectures/                  # Python concepts, in learning order
│   ├── 01_basics/
│   ├── 02_conditionals_loops/
│   ├── 03_lists_arrays/
│   ├── 04_strings/
│   ├── 05_functions/
│   ├── 06_dicts_sets_tuples/
│   ├── 07_oop/
│   ├── 08_exceptions_files/
│   ├── 09_iterators_generators/
│   └── 10_comprehensions_lambdas/
├── dsa/                       # Problems grouped by pattern / topic
│   ├── 01_arrays/  02_strings/  03_hashing/  04_two_pointers/
│   ├── 05_sliding_window/  06_prefix_sum/  07_binary_search/  08_sorting/
│   ├── 09_recursion_backtracking/  10_stack_queue/  11_linked_list/
│   ├── 12_trees/  13_heap/  14_graphs/  15_greedy/
│   └── 16_dynamic_programming/  17_bit_manipulation/
├── docs/                      # notes & interview guides
├── templates/problem_template.py   # copy this for every new problem
├── pyproject.toml             # deps + pytest/ruff config
└── poetry.toml                # tells Poetry to create .venv inside this folder
```

## Guides

- [Python Project Setup & Running Code — Interview Guide](docs/python-setup-interview-guide.md):
  environments, ways to run code, FastAPI setup, interview Q&A, cheat sheet.

## Setup

Requires Python 3.12+ and [Poetry](https://python-poetry.org/) 2.x.

```bash
# one-time: install Poetry (either works)
uv tool install poetry
# or: curl -sSL https://install.python-poetry.org | python3 -

# install deps into ./.venv
poetry install
```

The virtualenv lives at `./.venv` (set in `poetry.toml`) and is git-ignored. VS Code picks it up
automatically via `.vscode/settings.json`.

## Daily use

```bash
# run one file as a script
poetry run python dsa/01_arrays/001_two_sum.py

# run every test
poetry run pytest

# run one topic / one file / match by name
poetry run pytest dsa/01_arrays
poetry run pytest dsa/01_arrays/001_two_sum.py
poetry run pytest -k two_sum

# lint + format
poetry run ruff check . --fix
poetry run ruff format .

# REPL for experimenting
poetry run ipython
```

Tip: activate the env once per terminal and skip the `poetry run` prefix:

```bash
source .venv/bin/activate     # or: eval $(poetry env activate)
```

## Adding a problem

1. Copy `templates/problem_template.py` into the topic folder, numbered:
   `dsa/04_two_pointers/003_container_with_most_water.py`
2. Fill in the docstring (link, approach, complexity), write the solution and tests.
3. `poetry run pytest dsa/04_two_pointers/003_container_with_most_water.py`

## Managing dependencies

```bash
poetry add sortedcontainers        # runtime dep
poetry add --group dev mypy        # dev-only tool
poetry remove <pkg>
poetry show --tree
```

Commit both `pyproject.toml` and `poetry.lock` so the env is reproducible.

## Progress

| Area | Done |
| --- | --- |
| Lectures | 1 |
| DSA | 1 |
