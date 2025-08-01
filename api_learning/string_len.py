from fastapi import FastAPI
app = FastAPI()
@app.get("/length")
def length(text: str):
    return {"length": len(text)}