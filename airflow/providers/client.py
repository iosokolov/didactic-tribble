import httpx

import env_vars


class ProviderClientA:
    base_url = env_vars.PROVIDER_A_URL

    async def post_search(self) -> httpx.Response:
        r = httpx.post(f'{self.base_url}/search')
        return r


class ProviderClientB:
    base_url = env_vars.PROVIDER_B_URL

    async def post_search(self) -> httpx.Response:
        r = httpx.post(f'{self.base_url}/search')
        return r
