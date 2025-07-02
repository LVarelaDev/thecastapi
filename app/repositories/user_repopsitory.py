from typing import List

from app.models.user import User


class UserRepository:
    async def create_user(self, user: User) -> User:
        new_user = await user.insert()
        return new_user

    async def get_all(self) -> List[User]:
        return await User.find_all().to_list()

    async def verify_username(self, username: str) -> bool:
        user = await User.find_one(User.username == username)
        return user is not None

    async def find_by_username(self, username: str):
        return await User.find_one((User.username == username))
