from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.db.init_db import init_db
from app.routers import users_controller, cats_controller


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users_controller.router)
app.include_router(cats_controller.router)
