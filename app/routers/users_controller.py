from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_user
from app.models.login_input import LoginInput
from app.models.user_input import UserInput
from app.repositories.user_repopsitory import UserRepository
from app.services.user_service import UserService

router = APIRouter()
user_repository = UserRepository()
user_service = UserService(user_repository)


@router.post("/users")
async def create_user(user: UserInput):
    return await user_service.create(user)


@router.get("/users")
async def get_all_users(current_user=Depends(get_current_user)):
    return await user_service.get_all()


@router.post("/login")
async def login(input: LoginInput):
    token = await user_service.authenticate_user(input)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token, "token_type": "bearer"}
