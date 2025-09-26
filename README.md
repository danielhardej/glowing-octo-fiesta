# Django REST API Project

A complete Django REST API project with admin interface and CI/CD pipeline.

## Features

- **Django REST Framework**: Full-featured REST API with browsable API interface
- **Admin Interface**: Django admin panel with custom configurations
- **Task Management**: Complete CRUD operations for task management
- **Authentication**: Session-based authentication with DRF
- **Testing**: Comprehensive test suite with model and API tests
- **CI/CD Pipeline**: GitHub Actions workflow with linting, testing, and security checks
- **Code Quality**: Black, isort, and flake8 for code formatting and linting
- **Security**: Bandit and safety checks for security vulnerabilities

## API Endpoints

- `GET/POST /api/tasks/` - List all tasks or create a new task
- `GET/PUT/PATCH/DELETE /api/tasks/{id}/` - Retrieve, update, or delete a specific task
- `POST /api/tasks/{id}/mark_completed/` - Mark a task as completed
- `GET /api/tasks/my_tasks/` - Get tasks assigned to the authenticated user
- `GET /api/users/` - List all users

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd glowing-octo-fiesta
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - API Root: http://127.0.0.1:8000/api/
   - Admin Interface: http://127.0.0.1:8000/admin/
   - Browsable API: http://127.0.0.1:8000/api/tasks/

## Testing

Run the test suite:
```bash
python manage.py test
```

## Code Quality

Format code with Black:
```bash
black .
```

Sort imports with isort:
```bash
isort .
```

Lint code with flake8:
```bash
flake8 .
```

Security check with bandit:
```bash
bandit -r .
```

## Models

### Task Model
- `title`: CharField (required)
- `description`: TextField (optional)
- `priority`: Choice field (low, medium, high)
- `status`: Choice field (todo, in_progress, completed)
- `assigned_to`: ForeignKey to User (optional)
- `created_at`: DateTimeField (auto)
- `updated_at`: DateTimeField (auto)
- `due_date`: DateTimeField (optional)

## Admin Interface

The Django admin interface provides:
- Task management with filtering and search
- User management
- Bulk operations
- Custom admin configurations

## CI/CD Pipeline

GitHub Actions workflow includes:
- **Testing**: Multi-version Python testing (3.9, 3.10, 3.11, 3.12)
- **Linting**: Code quality checks with flake8, black, and isort
- **Security**: Security vulnerability scanning with bandit and safety

## Architecture

```
apiproject/
├── apiproject/          # Django project settings
│   ├── settings.py      # Main configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI application
├── tasks/               # Tasks Django app
│   ├── models.py        # Task model
│   ├── views.py         # API views
│   ├── serializers.py   # API serializers
│   ├── admin.py         # Admin configuration
│   ├── tests.py         # Test cases
│   └── urls.py          # App URLs
├── .github/workflows/   # CI/CD pipeline
├── requirements.txt     # Production dependencies
└── manage.py           # Django management script
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is open source and available under the MIT License.