# Django Project with Real-time Chat Feature - Installation Guide

This guide will help you set up and run this Django project with a real-time chat feature on Windows, macOS, or Linux.

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Installation Steps

### Step 1: Clone or Download the Repository

**Option 1: Clone with Git**
```bash
git clone https://github.com/modysosa/Base-React-Django.git
cd Base-React-Django
```

**Option 2: Download ZIP**
- Download the ZIP file from GitHub
- Extract it to your preferred location
- Open a terminal/command prompt and navigate to the extracted folder

### Step 2: Set Up a Virtual Environment

#### Windows
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

#### macOS/Linux
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# If requirements.txt is not available, install these packages:
pip install django==4.1.8
pip install Pillow
```

### Step 4: Apply Migrations

```bash
# Apply migrations to set up the database
python manage.py migrate
```

### Step 5: Create a Superuser (Admin)

```bash
# Create an admin user to manage the application
python manage.py createsuperuser
```
Follow the prompts to create your admin username, email, and password.

### Step 6: Run the Development Server

```bash
# Start the Django development server
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/

## Accessing the Application

- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Using the Chat Feature

1. Register at least two user accounts or use the admin account plus another account
2. Log in with one account
3. Open an incognito/private window and log in with another account
4. The chat window appears at the bottom right of the screen for logged-in users
5. Select a user from the list to start chatting
6. Use the emoji button to add emojis to your messages

## Troubleshooting

### Database Issues
If you encounter database issues, try:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files Not Loading
If static files (CSS, JS) are not loading properly:
```bash
python manage.py collectstatic
```

### Port Already in Use
If port 8000 is already in use, specify a different port:
```bash
python manage.py runserver 8080
```

## Platform-Specific Notes

### Windows
- Use backslashes (`\`) for file paths in commands
- If Python is not in your PATH, use the full path to Python executable

### macOS/Linux
- Use forward slashes (`/`) for file paths
- You might need to use `python3` instead of `python` depending on your setup
- You might need to use `sudo` for some commands if you encounter permission issues

## Additional Information

- The chat feature uses Django's built-in authentication system
- Messages are stored in the database and retrieved when users select a conversation
- The emoji picker is implemented with pure JavaScript and CSS, no external libraries required

## Need Help?

If you encounter any issues or have questions, please open an issue on the GitHub repository or contact the project maintainer.

Happy chatting!
