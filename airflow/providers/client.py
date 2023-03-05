import httpx

import settings


class ProviderClientA:
    base_url = settings.PROVIDER_A_URL

    async def post_search(self) -> httpx.Response:
        r = httpx.post(f'{self.base_url}/search', timeout=settings.PROVIDER_A_TIMEOUT)
        return r


class ProviderClientB:
    base_url = settings.PROVIDER_B_URL

    async def post_search(self) -> httpx.Response:
        r = httpx.post(f'{self.base_url}/search', timeout=settings.PROVIDER_B_TIMEOUT)
        return r
