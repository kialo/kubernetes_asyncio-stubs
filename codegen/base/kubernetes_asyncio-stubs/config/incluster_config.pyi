from typing import Optional

from ..client import Configuration

def load_incluster_config(
    client_configuration: Optional[Configuration] = ..., try_refresh_token: bool = ...
) -> None: ...
