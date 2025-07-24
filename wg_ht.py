from fastapi import FastAPI
app = FastAPI()
@app.get("/bmi")
def bmi(weight: float, height: float):
    return {"bmi": weight / (height * height)}

@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}