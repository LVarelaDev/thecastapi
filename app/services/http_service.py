import httpx
from fastapi import HTTPException

API_URL = "https://api.thecatapi.com/v1"
API_KEY = "live_JBT0Ah0Nt12iyl2IpjQVLDWjcLk0GQwf4zI9wBMfmfejKm"

HEADERS = {"x-api-key": API_KEY}


class Http_Service:
    def __init__(self):
        self.client = httpx.AsyncClient(headers=HEADERS)

    async def get_all_breeds(self):
        response = await self.client.get(f"{API_URL}/breeds")
        self._check_response(response)
        return response.json()

    async def get_breed_by_id(self, breed_id: str):
        response = await self.client.get(f"{API_URL}/breeds/{breed_id}")
        self._check_response(response, allow_404=True)
        return response.json()

    async def search_breeds(self, query: str):
        response = await self.client.get(
            f"{API_URL}/breeds/search", params={"q": query}
        )
        self._check_response(response)
        return response.json()

    def _check_response(self, response, allow_404=False):
        if allow_404 and response.status_code == 404:
            raise HTTPException(status_code=404, detail="Breed not found")
        elif response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error from external API")
