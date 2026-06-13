# 🚀 100 Days of Python API Challenge

Build one API every day and gradually move from beginner to advanced topics.

This challenge covers:

* REST APIs
* Databases
* Authentication
* Caching
* External APIs
* AI APIs
* Real-time systems
* Microservices

---

# 🎂 Age Calculator API (FastAPI)

A simple FastAPI project that calculates a person's age based on their birth date.

## 📚 What You'll Learn

* ✅ Creating API endpoints with FastAPI
* ✅ Handling query parameters
* ✅ Working with Python's `datetime` module
* ✅ Returning JSON responses
* ✅ Running a FastAPI server with Uvicorn
* ✅ Testing APIs using Swagger UI

---

## 📂 Project Structure

```
age_calculator_api/
│
├── app.py
├── requirements.txt
```

---

## 🚀 Step 1: Create Project Folder

```bash
mkdir age_calculator_api
cd age_calculator_api
```

---

## 🚀 Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## 🚀 Step 3: Install Dependencies

```bash
pip install fastapi uvicorn
```

(Optional)

Create `requirements.txt`

```bash
pip freeze > requirements.txt
```

---

## 🚀 Step 4: Create `main.py`

```python
from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Age Calculator API is running 🚀"}

@app.get("/age")
def calculate_age(year: int, month: int, day: int):
    today = date.today()
    birth_date = date(year, month, day)

    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return {
        "birth_date": birth_date,
        "age": age
    }
```

---

## 🚀 Step 5: Run the Server

```bash
uvicorn main:app --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

---

## 🌐 API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Age Calculator API is running 🚀"
}
```

---

### Age Calculator Endpoint

```http
GET /age?year=2000&month=5&day=10
```

Example:

```
http://127.0.0.1:8000/age?year=2000&month=5&day=10
```

Response:

```json
{
  "birth_date": "2000-05-10",
  "age": 25
}
```

---

## 📖 Interactive API Documentation

FastAPI automatically generates Swagger UI.

Open:

```
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

---

## 🛠 Technologies Used

* Python 3
* FastAPI
* Uvicorn
* datetime


