from fastapi import FastAPI
app = FastAPI()
@app.get("/can_vote")
def check_age(age: int):
    # return {"is_adult": age >= 18}
    if age>=18:
        return {"can_vote": True}
    else:
        return {"can_vote": False}