# Django + React with chat

A Django application with server-rendered account pages, a React demo loaded from CDNs, JSON endpoints, and chat using HTTP polling.

## Structure

| Path | Responsibility |
| --- | --- |
| `manage.py` | Django management commands |
| `mysite/` | Settings, root URLs, WSGI and ASGI entry points |
| `core/` | Home template, example API, Category and Item models |
| `core/static/js/app.js` | React JSX rendered using browser-side Babel |
| `users/` | Registration, login/logout, profiles, forms and profile signals |
| `chat/` | Messages, conversation endpoints, user list and chat panel |
| `static/css/chat.css` | Chat styling |
| `.github/workflows/` | Manual runner check and automatic deployment on `main` |

SQLite is the default database. There is no separate frontend server, Node build, Redis, WebSocket consumer, or Django REST Framework dependency. JSON APIs use Django's `JsonResponse`. The `ci.yml` workflow only checks runner identity; it does not currently execute tests.

## Local development

See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for setup. Use Python 3.12 with the dependencies pinned in `requirements.txt`.

After installing dependencies and applying migrations:

```powershell
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

Open http://127.0.0.1:8000/. Browser-side libraries require internet access.

## Verification

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run
.\.venv\Scripts\python.exe manage.py test
```

Tests cover the home/API endpoints, registration, profile creation and updates, login, CSRF-protected logout, chat authentication, sending and reading messages, conversation isolation, empty-message rejection, and the user list.

## Review and deployment

Before any push to `main`, present the changes and test results to the user and wait for approval. Pushing to `main` automatically triggers deployment to the configured self-hosted Linux runner.

See [PROJECT_REVIEW.md](PROJECT_REVIEW.md) for the local setup review and remaining limitations.
