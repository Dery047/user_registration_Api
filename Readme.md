## 🚧 Project Under Active Development

This project is currently **under maintenance and development**. I’m fixing bugs and implementing new features to improve its functionality. Thank you for your understanding!

### 🔧 In Progress:
- ✉️ Email verification system
- 🧪 Basic front-end view for API testing.




# Django JWT Authentication API (Sigue bajando para el README en español)

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
|--------|-----------------------|-----------------------------------|
| POST   | `/api/register/`      | Register a new user                |
| POST   | `/api/login/`         | Login and get JWT tokens           |
| POST   | `/api/logout/`        | Logout and blacklist the token     |
| POST   | `/api/token/`         | Obtain access & refresh tokens     |
| POST   | `/api/token/refresh/` | Refresh access token               |
| POST   | `/api/token/verify/`  | Verify if a token is still valid   |

Note: The password field is visible in the DRF browsable API and may also appear in browser autocomplete. In a real-world frontend, it would be rendered as a hidden password field.

---

## Setup Instructions 

Clone and run this project locally if you want to test it :)

```bash
# Clone the repo
git clone https://github.com/your-username/user_registration_Api.git
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
````

---

# API de Autenticación JWT con Django

Una API backend simple y segura construida con Django y Django REST Framework para manejar el registro de usuarios, inicio de sesión (con JWT), refresco de tokens y cierre de sesión. La API utiliza SimpleJWT para gestionar los tokens de acceso y refresco.

---

## Funcionalidades

* Registro de usuarios
* Inicio de sesión con usuario y contraseña
* Autenticación basada en JWT (tokens de acceso y refresco)
* Soporte para refrescar tokens
* Cierre de sesión con lista negra de tokens de refresco
* Endpoint para verificar la validez de un token
* Estructura limpia, modular y lista para escalar

---

## Tecnologías usadas

* Python 3.12
* Django 5.2
* Django REST Framework
* SimpleJWT (autenticación JWT)

---

## Endpoints

| Método | Ruta                  | Descripción                         |
| ------ | --------------------- | ----------------------------------- |
| POST   | `/api/register/`      | Registrar un nuevo usuario          |
| POST   | `/api/login/`         | Iniciar sesión y obtener tokens JWT |
| POST   | `/api/logout/`        | Cerrar sesión y bloquear el token   |
| POST   | `/api/token/`         | Obtener tokens de acceso y refresco |
| POST   | `/api/token/refresh/` | Refrescar el token de acceso        |
| POST   | `/api/token/verify/`  | Verificar si un token es válido     |

Nota: El campo de contraseña es visible en la API navegable de DRF y puede aparecer en el autocompletado del navegador. En un frontend real, se mostrará como un campo oculto para contraseñas.

---

## Instrucciones para configurar

Clona y ejecuta este proyecto localmente si quieres probarlo :)

```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/user_registration_Api
cd user_registration_Api

# Crea un entorno virtual
python -m venv env
env\Scripts\activate # o si usas Mac: env/bin/activate 

# Instala las dependencias
pip install -r requirements.txt

# Aplica las migraciones
python manage.py migrate

# Ejecuta el servidor de desarrollo y listo ;)
python manage.py runserver
```

---

Solo uso lógica backend, no hay vistas frontend. Además, planeo actualizar el código agregando verificación de correo electrónico y recuperación de contraseña.

```


```


