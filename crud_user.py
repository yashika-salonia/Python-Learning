from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
users = []
class User(BaseModel):
    name: str
    email: str
@app.post("/user")
def create_user(user: User):
    users.append(user.dict())
    return user
@app.get("/users")
def list_users():
    return users