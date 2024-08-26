#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from base64 import b64encode, b64decode
from os import urandom, getenv
from time import time
from random import randint
import hashlib

SECRET = urandom(32)
FLAG = getenv("FLAG")


class LoginData(BaseModel):
    username: str
    password: str


app = FastAPI()


def create_token(username: str, admin: bool = False) -> str:
    current_time = int(time())

    header = "typ:JWT;alg:HS256;".encode()
    data = f"sub:{randint(1000000, 9999999)};name:{username};iat:{current_time};exp:{current_time + 60 * 60 * 24};".encode(
    )

    signature = hashlib.sha256(SECRET + header + data).digest()

    b64_header = b64encode(header).decode()
    b64_data = b64encode(data).decode()
    b64_signature = b64encode(signature).decode()

    return f"{b64_header}.{b64_data}.{b64_signature}"


def validate_token(token: str) -> bool:
    try:
        header, data, signature = token.split(".")
        header = b64decode(header.encode())
        data = b64decode(data.encode())

        validate_signature = hashlib.sha256(SECRET + header + data).digest()

        return b64encode(validate_signature).decode() == signature
    except ValueError:
        return False


@app.post("/api/login")
def login(data: LoginData, response: Response):
    username = data.username
    password = data.password

    if username == "james" and password == "web":
        response.set_cookie(key="session",
                            value=create_token(username),
                            httponly=True,
                            samesite="strict")
        return {"message": f"Hello {username}!"}

    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/api/flag")
def flag(request: Request):
    token = request.cookies.get("session")

    if token is None:
        raise HTTPException(status_code=401, detail="Missing token")

    if not validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    data = b64decode(token.split(".")[1])

    if b"name:administrator;" in data:
        return {"message": FLAG}

    return {"message": "Womp womp no flag for you"}


app.mount('/', StaticFiles(directory='public', html=True), name='public')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
