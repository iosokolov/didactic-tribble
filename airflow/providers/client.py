import httpx

import settings


class ProviderClientA:
    base_url = env_vars.PROVIDER_A_URL

    async def post_search(self) -> httpx.Response:
        r = httpx.post(f'{self.base_url}/search', timeout=env_vars.PROVIDER_A_TIMEOUT)
        return r


class ProviderClientB:
    base_url = env_vars.PROVIDER_B_URL

    async def post_search(self) -> httpx.Response:
        r = httpx.post(f'{self.base_url}/search', timeout=env_vars.PROVIDER_B_TIMEOUT)
        return r
