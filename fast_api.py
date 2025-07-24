# for heavy model tasking it is 1st priority to use fastapi
# fastapi is a modern, fast (high-performance), web framework for building APIs with Python
# works on asynchronous programming
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}