# Django Project with React Integration and Real-time Chat

A full-stack web application built with Django and React. This project includes user authentication, profile management, a React frontend, and a real-time chat feature with emoji support.

## Features

- User authentication (register, login, logout)
- User profile management
- Real-time chat between users with emoji support
- React integration for dynamic frontend
- RESTful API endpoints
- Bootstrap for responsive design

## Prerequisites

- Python 3.8 or higher
- Django 4.1 or higher
- Pillow (for image processing)
- Web browser

## Installation

1. Clone the repository or download the source code:

```bash
git clone <repository-url>
cd django_project
```

2. Create and activate a virtual environment (optional but recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install django
pip install Pillow
```

4. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):

```bash
python manage.py createsuperuser
```

   Recommended default credentials for development:
   - Username: `admin`
   - Email: `admin@example.com`
   - Password: `adminpassword123`
   
   Note: In a production environment, always use a strong, unique password.

## Running the Project

1. Start the development server:

```bash
python manage.py runserver
```

2. Open your web browser and navigate to:
   - http://127.0.0.1:8000/ - Homepage with React integration
   - http://127.0.0.1:8000/admin/ - Django admin interface
   - http://127.0.0.1:8000/users/register/ - User registration
   - http://127.0.0.1:8000/users/login/ - User login

## Project Structure

- `core/` - Main application with React integration
- `users/` - User authentication and profile management
- `chat/` - Real-time chat functionality with emoji support
- `mysite/` - Project settings and main URL configuration
- `media/` - User-uploaded files (profile pictures)
- `static/` - Static files (CSS, JavaScript, images)

## User Authentication

The project includes a complete user authentication system:

1. Register a new account at `/users/register/`
2. Login at `/users/login/`
3. View and edit your profile at `/users/profile/`
4. Logout at `/users/logout/`

## Chat Feature

The project includes a WhatsApp-like chat feature:

1. Chat window appears at the bottom right for authenticated users
2. Select a user from the list to start a conversation
3. Send messages with text and emojis
4. View message history and unread message indicators
5. Minimize/maximize the chat window as needed

## React Integration

The project uses React for the frontend, with components loaded directly from Django templates. The React code is located in `core/static/js/app.js`.

## Database Configuration

By default, the project uses SQLite for development. To use PostgreSQL or another database:

1. Install the appropriate database adapter (e.g., `psycopg2-binary` for PostgreSQL)
2. Update the `DATABASES` setting in `mysite/settings.py`

## Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure a production-ready database
3. Set up static files serving
4. Use a production WSGI server like Gunicorn
5. Configure a reverse proxy like Nginx

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django - The web framework used
- React - Frontend library
- Bootstrap - CSS framework
