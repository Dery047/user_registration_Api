# Django JWT Authentication API

A simple and secure backend API built with Django and Django REST Framework to handle user registration, login (with JWT) token refresh, and logout. The API uses SimpleJWT for managing access and refresh tokens.

---

## Features

- User registration
- Login using username & password.
- JWT-based authentication (access & refresh tokens)
- Refresh token support.
- Logout by blacklisting refresh tokens
- Token verification endpoint.
- Clean, modular and ready-to-scale structure

---

## Tech Stack

- Python 3.12
- Django 5.2
- Django REST Framework
- SimpleJWT (JWT authentication).

---

## Endpoints

| Method | Endpoint              | Description                         |
|--------|------------------------|-------------------------------------|
| POST   | `/api/register/`       | Register a new user                 |
| POST   | `/api/login/`          | Login and get JWT tokens            |
| POST   | `/api/logout/`         | Logout and blacklist the token      |
| POST   | `/api/token/`          | Obtain access & refresh tokens      |
| POST   | `/api/token/refresh/`  | Refresh access token                |
| POST   | `/api/token/verify/`   | Verify if a token is still valid    |

Note: The password field is visible in the DRF browsable API and may also appear in browser autocomplete. In a real-world frontend, it will be rendered as a hidden password field.

---

## Setup Instructions 


Clone and run this project locally if you want to test it :)

```bash
# Clone the repo
git clone https://github.com/your-username/user_registration_Api
cd user_registration_Api

# Create the virtual environment
python -m venv env
env\Scripts\activate # or if you use Mac: env/bin/activate 

# Install dependencies (important)
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# and run it ;)
python manage.py runserver


#Im only usign backend logic, no frontend views, also i will be updating the code by adding email verification and password reset
