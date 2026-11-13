# Project workflow

- Django serves the templates, JSON endpoints, and static React JSX; there is no npm build.
- Use Python 3.12 and install the pinned dependencies from `requirements.txt` in `.venv`.
- Before handing off changes, run `manage.py check`, `manage.py makemigrations --check --dry-run`, and `manage.py test` with the virtual environment's Python.
- Before any push to `main`, show the user the changes and test results and wait for their approval. A push to `main` triggers deployment via `.github/workflows/deploy.yml`.
- Preserve existing local SQLite data and uploaded media. Do not commit credentials or virtual environments.
