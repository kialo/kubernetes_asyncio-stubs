import io

from aiohttp import ClientResponse
from multidict import CIMultiDictProxy

class RESTResponse(io.IOBase):
    aiohttp_response: ClientResponse
    data: bytes
    reason: str
    status: int

    def __init__(self, resp: ClientResponse, data: bytes) -> None: ...
    def getheaders(self) -> CIMultiDictProxy: ...
    def getheader(self, name: str, default: bool) -> str: ...

class RESTClientObject: ...
