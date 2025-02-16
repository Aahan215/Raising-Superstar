# Prodigy Programs - Django Backend

This project implements a REST API using Django and Django REST Framework (DRF) for managing "5-minute per day" programs. Users can view daily activities, track progress, and mark activities as complete.

## Features
- View all available programs.
- Fetch daily activities for a given program.
- Mark activities as completed by users.
- Retrieve user progress within a program.
- Token-based authentication using JWT.

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT Authentication (Simple JWT)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd <repo-folder>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database (PostgreSQL)
Update `settings.py` with your PostgreSQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

## API Endpoints

### 1. Obtain JWT Token
**POST /api/token/**
```json
{
  "username": "user1",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

### 2. Refresh JWT Token
**POST /api/token/refresh/**
```json
{
  "refresh": "jwt_refresh_token"
}
```
**Response:**
```json
{
  "access": "new_jwt_access_token"
}
```

### 3. List All Programs
**GET /api/programs/**
```json
[
  { "id": 1, "name": "Morning Wellness", "description": "Daily exercises." }
]
```

### 4. Get Activities for a Program (Day 14-21)
**GET /api/programs/{program_id}/activities/?start_day=14&end_day=21**
```json
{
  "day": 14,
  "activities": [
    { "id": 3, "title": "Morning Stretching", "description": "5-minute exercise." }
  ]
}
```

### 5. Mark an Activity as Completed
**POST /api/user-activities/**
```json
{ "activity_id": 3 }
```
**Response:**
```json
{ "message": "Activity marked as complete" }
```

### 6. Get User Progress
**GET /api/user-activities/{user_id}/programs/{program_id}/**
```json
{
  "completed_days": [14, 15, 17],
  "pending_days": [16, 18, 19]
}
```

## Running Tests
To run tests, execute:
```bash
python manage.py test
```

---

