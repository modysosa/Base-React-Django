# Local setup review

## Architecture

Requests enter through `mysite/urls.py` and route to `core`, `users`, or `chat`. Django templates share `core/base.html`. The home template loads React 18 and Babel from CDNs, then renders `core/static/js/app.js`, which calls `/api/example/`. Authenticated pages include the chat panel; its JavaScript fetches users and messages and polls every 10 seconds. Messages persist in SQLite. User creation signals create a one-to-one profile; Pillow resizes uploaded profile photos.

## Setup changes

- Added `.venv/`, `.env`, and generated `staticfiles/` to Git exclusions.
- Updated installation instructions to match the pinned dependencies and actual application structure, without a default admin password.
- Replaced the GET logout link with a CSRF-protected POST form, as required by the installed Django version.
- Added 12 integration tests across home/API, accounts, and chat.
- Recorded the review-before-push requirement in `AGENTS.md`.

## Remaining findings

- Chat inserts message text into `innerHTML` in both message loading and sending callbacks. This permits stored HTML/script injection and should be corrected using text nodes before exposing the application to untrusted users.
- Settings contain a development secret and `DEBUG=True`; production settings and dependency security review are outside this local setup.
- `media/default.jpg` is missing, so the default profile image can return 404.
- External CDNs are required to render the React demo and other frontend assets.
- The manual CI workflow runs `whoami`, not tests. Deployment runs automatically on a push to `main` without a test job in these workflow definitions.
- The chat API broadly catches exceptions and returns their messages; payload validation and error handling need a separate review.

Existing SQLite data was preserved. Test accounts are created only in Django's separate test database. No deployment or push is needed for local setup.

## Verification results (2026-11-13)

- Environment: CPython 3.12.13 in `.venv`, with the pinned requirements installed.
- `manage.py check`: no issues.
- `manage.py makemigrations --check --dry-run`: no changes detected.
- `manage.py migrate --noinput`: no migrations to apply to the existing database.
- `manage.py test --verbosity 2`: all 12 tests passed using an in-memory database.
- `python -m pip check`: no broken requirements.
- `git diff --check`: passed.
- Live HTTP checks: home, example API, registration, login, React JSX and chat CSS all returned 200 at `127.0.0.1:8000`.
- Browser rendering and interactive frontend behavior were not manually verified.

The local server was started in the background with `--noreload`; changes to
Python code require a restart. Its PID is saved in `.venv/server.pid` and logs
are in `.venv/server.stdout.log` and `.venv/server.stderr.log`. To stop it, verify
the recorded PID still belongs to this project's runserver process, then use
`Stop-Process -Id <PID>`. For normal development, run the foreground command in
the installation guide after stopping the background server.
