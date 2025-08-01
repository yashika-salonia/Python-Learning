from fastapi import FastAPI
app = FastAPI()
@app.get("/reverse")
def reverse(text: str):
    return {"reversed": text[::-1]}