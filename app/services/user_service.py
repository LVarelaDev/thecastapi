from datetime import timedelta
from typing import List
from app.core.security import create_access_token
from app.models.login_input import LoginInput
from app.models.user_input import UserInput
from app.repositories.user_repopsitory import UserRepository
from passlib.context import CryptContext
import re
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create(self, data: UserInput) -> User:
        username_generated = await self.generate_unique_username(
            data.name, data.lastname
        )

        password = self.hash_password(data.password)

        newUser = User(
            name=data.name,
            lastname=data.lastname,
            email=data.email,
            password=password,
            username=username_generated,
        )

        user = await self.repository.create_user(newUser)
        return user

    async def get_all(self) -> List[User]:
        user = await self.repository.get_all()
        return user

    async def verify_username(self, username: str) -> bool:
        username_valid = await self.repository.verify_username(username)
        return username_valid

    async def generate_unique_username(self, name: str, lastname: str) -> str:
        base = f"{name.lower()}.{lastname.lower()}"
        base = re.sub(r"[^a-z.]", "", base)

        candidate = base
        counter = 1

        while await self.verify_username(candidate):
            candidate = f"{base}{counter}"
            counter += 1

        return candidate

    async def authenticate_user(self, username: str, password: str) -> str:
        user = await self.repository.find_by_username(username, password)
        if not user:
            return None

        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=timedelta(minutes=30)
        )
        return access_token

    async def authenticate_user(self, input: LoginInput):
        user = await self.repository.find_by_username(input.username)
        if not user:
            return None

        print(user)
        if self.verify_password(input.password, user.password) == False:
            return None

        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=timedelta(minutes=30)
        )
        return access_token

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
