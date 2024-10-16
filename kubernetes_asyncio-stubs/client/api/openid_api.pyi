import kubernetes_asyncio.client
import typing

class OpenidApi:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_service_account_issuer_open_id_keyset(self) -> str: ...
