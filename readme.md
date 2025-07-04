# 🎮 GameNet Backend

A Django-based backend API for managing customers, employees, and subscription systems in a game net environment. Built using **Django**, **NinjaExtra**, and **JWT** for authentication.

---

## 📁 Project Structure

```
armemami2001-gamenet_backend/
├── manage.py
├── rav.yaml
├── requirements.txt
├── Gamenet_backend/
│   ├── api.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── usersapi/
    ├── controller.py       # All API logic
    ├── models.py           # Customer & Worker models
    ├── schema.py           # Request/Response validation
    ├── router.py           # Role-based access via JWT
    └── migrations/
```

---

## ⚙️ Setup

```bash
# Run venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start dev server
python manage.py runserver 8001
```

---

## 🔐 JWT Authentication

- Login to get tokens: `/api/auth/login`
- Protected endpoints require `Authorization: Bearer <access_token>`

---

## 📦 API Endpoints

### 🔐 `POST /api/auth/login`

Login and receive JWT tokens.

**Request**
```json
{
  "username": "admin",
  "password": "1234"
}
```

**Response**
```json
{
  "access": "eyJ...",
  "refresh": "eyJ..."
}
```

---

### 👤 `POST /api/customer/create-customer`

Register a new customer account.

**Request**
```json
{
  "username": "ali",
  "password": "testpass"
}
```

**Response**
```json
{
  "id": 3,
  "subs": "2025-07-04",
  "username": "ali",
  "days_remaining": 29
}
```

---

### 👤 `GET /api/customer/me`

Get current customer profile (requires `JWT`).

**Response**
```json
{
  "id": 3,
  "subs": "2025-07-04",
  "username": "ali",
  "days_remaining": 29
}
```

---

### 🧑‍💼 `POST /api/employee/add_employee`

Create a new employee account.

---

### 🧑‍💼 `GET /api/employee/me`

Get profile of currently logged-in employee.

---

### 🧑‍💼 `PUT /api/employee/worktime/{pk}`

Update worktime for an employee.

**Request**
```json
{
  "worktime": "8:00 AM - 4:00 PM"
}
```

---

### 🧑‍💼 `GET /api/employee/`

List all employees.

---

### 🧑‍💼 `GET /api/employee/addsub`

List all customers (employee view).

---

### 🧑‍💼 `PUT /api/employee/addsub/{pk}`

Update a customer’s subscription.

**Request**
```json
{
  "subtime": "2025-07-30"
}
```

---

## 🧠 Role-Based Access

Roles are embedded in JWTs:

```json
{
  "username": "admin",
  "role": "employee"
}
```

Use custom `IsEmployee` guard for employee-only routes.
