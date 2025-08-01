from fastapi import FastAPI
import random
app = FastAPI()
quotes = ["Keep going!", "Never give up!", "Stay positive."]
@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}