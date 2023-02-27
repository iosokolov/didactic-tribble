from abc import ABC, abstractmethod
from typing import List

from providers.client import ProviderClientA


class ProviderServiceBase(ABC):
    @abstractmethod
    async def post_search(self):
        ...

    def parse(self, data):
        return data


class ProviderServiceA(ProviderServiceBase):
    async def post_search(self) -> List[dict]:
        client = ProviderClientA()
        response = await client.post_search()
        response.raise_for_status()
        return self.parse(response.json())


class ProviderServiceB(ProviderServiceBase):
    async def post_search(self) -> List[dict]:
        client = ProviderClientA()
        response = await client.post_search()
        response.raise_for_status()
        return self.parse(response.json())
