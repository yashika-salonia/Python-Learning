from fastapi import FastAPI
app = FastAPI()
@app.get("/evenodd")
def even_odd(num: int):
    return {"type": "even" if num % 2 == 0 else "odd"}