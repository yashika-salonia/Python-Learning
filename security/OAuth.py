from fastapi.security import OAuth2PasswordBearer

from fastapi import Depends, FastAPI
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/oauth-protected")
def oauth_route(token: str = Depends(oauth2_scheme)):
    return {"token": token}