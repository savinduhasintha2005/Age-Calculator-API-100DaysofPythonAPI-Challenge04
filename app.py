from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Welcome to Age Calculator API"}

@app.get("/age")
def calculate_age(year:int,month:int,day:int):
    today = date.today()
    birth_date = date(year,month,day)

    age = today.year - birth_date.year

    if (today.month , today.day) < (birth_date.month , birth_date.day):
        age -= 1
        return {
            "birth_date" : birth_date,
            "age" : age
        }
    return None



