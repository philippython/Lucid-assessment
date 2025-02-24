# FastAPI Authentication API

This is a simple FastAPI authentication API that provides user registration (signup) and login functionality using JWT tokens. The system stores users in memory and supports authentication via email and password.

## Features

- **User Registration**: Users can sign up using email and password.
- **User Login**: Authenticates users and returns a JWT token.
- **Token-Based Authentication**: Uses JWT for secure API access.
- **User Profile**: Retrieves the authenticated user's profile.

## Technologies Used

- FastAPI
- Pydantic
- Passlib (for password hashing)
- PyJWT (for JWT authentication)
- UUID (for user ID generation)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/fastapi-auth-app.git
   cd fastapi-auth-app
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install fastapi uvicorn passlib[bcrypt] pyjwt
   ```

## Running the Application

Start the FastAPI server using Uvicorn:
```sh
uvicorn main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

### **User Signup**
Registers a new user.

- **Endpoint:** `POST /signup/`
- **Request Body:**
  ```json
  {
    "email": "test@example.com",
    "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "your_jwt_token_here",
    "token_type": "bearer"
  }
  ```

### **User Login**
Authenticates a user and returns a JWT token.

- **Endpoint:** `POST /login/`
- **Request Body (Form Data):**
  ```sh
  username=test@example.com&password=securepassword
  ```
- **Response:**
  ```json
  {
    "access_token": "your_jwt_token_here",
    "token_type": "bearer"
  }
  ```

### **Get Current User**
Returns the authenticated user's profile.

- **Endpoint:** `GET /users/me/`
- **Headers:**
  ```sh
  Authorization: Bearer <TOKEN>
  ```
- **Response:**
  ```json
  {
    "id": "user-uuid-here",
    "email": "test@example.com"
  }
  ```

## Testing with cURL

### **Signup**
```sh
curl -X POST "http://127.0.0.1:8000/signup/" \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com", "password": "securepassword"}'
```

### **Login**
```sh
curl -X POST "http://127.0.0.1:8000/login/" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=test@example.com&password=securepassword"
```

### **Get User Profile**
```sh
curl -X GET "http://127.0.0.1:8000/users/me/" \
     -H "Authorization: Bearer <TOKEN>"
```

## Next Steps
- Store users in a **real database** (PostgreSQL, MySQL, MongoDB).
- Implement **refresh tokens** for better authentication handling.
- Add **email verification** and **password reset functionality**.
