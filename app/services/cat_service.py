from app.services.http_service import Http_Service


class CatsService:
    def __init__(self, http_service: Http_Service):
        self.http_service = http_service

    async def get_all_breeds(self):
        return await self.http_service.get_all_breeds()

    async def get_breed_by_id(self, breed_id: str):
        return await self.http_service.get_breed_by_id(breed_id)

    async def search_breeds(self, query: str):
        return await self.http_service.search_breeds(query)
