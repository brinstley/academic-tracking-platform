# Academic Tracking Platform

A Django-based web application for managing academic institutions with role-based user management for students, teachers, and school administrators.

## Features

- User management with role-based access (Student, Teacher, School Admin)
- User profiles with matricule numbers
- Django admin interface for data management
- SQLite database for easy setup and development

## Tech Stack

- **Framework**: Django 5.2.10
- **Language**: Python 3.x
- **Database**: SQLite3
- **ASGI Server**: asgiref 3.11.0

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/brinstley/academic-tracking-platform.git
cd academic-tracking-platform
```

### 2. Create a virtual environment

**On macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

**On Windows:**
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (admin account)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username, email, and password.

## Running the Application

### Start the development server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### Access points

- **Home/Accounts**: `http://127.0.0.1:8000/accounts/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

## Project Structure

```
academic-tracking-platform/
├── accounts/              # User management app
│   ├── migrations/        # Database migrations
│   ├── models.py          # User model with roles
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   └── ...
├── eduapp/                # Main project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── db.sqlite3             # SQLite database
```

## User Roles

The platform supports three user roles:

- **STUDENT**: Student users
- **TEACHER**: Teacher/instructor users
- **SCHOOL_ADMIN**: School administrator users

## Development

### Create new migrations after model changes

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run tests

```bash
python manage.py test
```

### Collect static files (for production)

```bash
python manage.py collectstatic
```

## Configuration

Key settings can be modified in `eduapp/settings.py`:

- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Add your domain names for production
- `SECRET_KEY`: Change to a secure random key in production
- `DATABASES`: Configure your production database

## Security Notes

⚠️ **Important for Production:**

1. Change the `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS` properly
4. Use a production-grade database (PostgreSQL, MySQL)
5. Set up proper static file serving
6. Enable HTTPS
7. Review all security settings

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Support

For issues and questions, please [open an issue](link-to-issues) on the repository.
