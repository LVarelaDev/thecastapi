from beanie import Document
from pydantic import EmailStr
from typing import Optional

class User(Document):
    name: str
    lastname: str
    username: str
    email: EmailStr
    password: str

    class Settings:
        name = "users"
