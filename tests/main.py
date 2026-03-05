
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}




class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user






"""
token: Annotated[str, Depends(oauth2_scheme)]

This means:
	•	token → parameter name
	•	str → expected type
	•	Depends(oauth2_scheme) → tells FastAPI:
	•	“Before calling this function, run oauth2_scheme”
	•	“Inject its result into token”

So effectively:
	1.	FastAPI sees this endpoint requires a dependency.
	2.	It runs oauth2_scheme.
	3.	oauth2_scheme extracts the Bearer token from the request header.
	4.	The token string gets passed into token.


    Equivalent older version without "Annotated"

    async def read_items(token: str = Depends(oauth2_scheme)):

    

"""