from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.services.cat_service import CatsService
from app.services.http_service import Http_Service


router = APIRouter(prefix="/breeds", tags=["Cats"])
http_service = Http_Service()
cats_service = CatsService(http_service)


@router.get("/")
async def get_all_breeds(current_user=Depends(get_current_user)):
    return await cats_service.get_all_breeds()


@router.get("/{breed_id}")
async def get_breed(breed_id: str, current_user=Depends(get_current_user)):
    return await cats_service.get_breed_by_id(breed_id)


@router.get("/search/{q}")
async def search_breeds(q: str, current_user=Depends(get_current_user)):
    return await cats_service.search_breeds(q)
