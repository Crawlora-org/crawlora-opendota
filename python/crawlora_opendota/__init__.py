"""Typed OpenDota client for the Crawlora hosted API."""

from .platform import OpenDotaClient, AsyncOpenDotaClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = OpenDotaClient
AsyncClient = AsyncOpenDotaClient
__version__ = '0.1.0'
DISPLAY_NAME = 'OpenDota'
PLATFORM = 'opendota'
CONTRACT_REVISION = 'sha256:bd541087bc32280cd45ea20c8afb0f976d4a9b54df109f589f4a858eb14b9c3a'

__all__ = [
    "OpenDotaClient", "AsyncOpenDotaClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
