# main.py
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


app = FastAPI()

bcrypt_context = CryptContext(
    schemes=["pbkdf2_sha256"],  # or "argon2"
    deprecated="auto"
)

from auth_roters import auth_router
from order_roters import order_router

app.include_router(auth_router)
app.include_router(order_router)



#run on terminal
    # uvicorn main:app -reload
# run on url website to make API teste
    # http://127.0.0.1:8000/docs#/pedidos 