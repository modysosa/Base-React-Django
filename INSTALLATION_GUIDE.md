# Local installation

Use Python 3.12 with the pinned dependencies in `requirements.txt`. Browser libraries load from CDNs and require internet access. There is no npm install or frontend build.

## Windows PowerShell

Run from the repository root:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

If the Python launcher points to a missing installation, use:

```powershell
uv venv --python 3.12 .venv
.\.venv\Scripts\python.exe -m ensurepip --upgrade
uv pip install --python .venv/Scripts/python.exe -r requirements.txt
```

Calling the environment's Python directly avoids PowerShell activation policy changes. For subsequent runs, only the `runserver` command is needed.

## macOS / Linux

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py check
.venv/bin/python manage.py test
.venv/bin/python manage.py runserver 127.0.0.1:8000
```

## Try the application

- Home: http://127.0.0.1:8000/
- JSON API: http://127.0.0.1:8000/api/example/
- Register: http://127.0.0.1:8000/users/register/
- Login: http://127.0.0.1:8000/users/login/
- Profile (login required): http://127.0.0.1:8000/users/profile/
- Admin: http://127.0.0.1:8000/admin/

Create your own account through registration. Admin access is optional: run `.\.venv\Scripts\python.exe manage.py createsuperuser` and choose your own credentials. Setup does not create accounts or default passwords.

For chat, register two accounts and sign in through separate browser sessions (for example, a normal window and a private window). Select the other user in the chat panel. The frontend polls every 10 seconds; it does not use WebSockets.

SQLite data lives in `db.sqlite3`; uploaded images live in `media/`. Preserve existing files. Tests use a separate in-memory database. The repository does not include `media/default.jpg`, so an account without an uploaded photo may show a broken image.

If port 8000 is occupied, use `runserver 127.0.0.1:8080`. Django serves static files automatically in local debug mode; `collectstatic` is not needed. Check schema consistency with `makemigrations --check --dry-run`; generate migrations only when intentionally changing models.

## Before publishing

Show the changes and test results to the user and wait for approval before any push to `main`. That push automatically triggers deployment. Current settings are for development and require a separate production configuration.
