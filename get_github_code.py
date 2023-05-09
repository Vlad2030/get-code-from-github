import base64
import httpx
import orjson
import aiohttp


class Request:
    def __init__(self) -> None:
        pass

    def request():
        pass

    async def async_request():
        pass


class JSON:
    def __init__(self) -> None:
        pass

    def loads():
        pass

    async def async_loads():
        pass


class Decode:
    def __init__(self) -> None:
        pass

    def b64():
        pass

    async def b64():
        pass


class GetCode:
    def __init__(
            self,
            user: str,
            repo: str,
            branch: str,
            file: str
    ) -> None:
        self.user: str = user
        self.repo: str = repo
        self.branch: str = branch
        self.file: str = file
        self.url: str = "https://api.github.com/repos/{}/{}/contents/{}?ref={}"

    def get_version():
        pass

    async def get_version():
        pass


def get_version(
        user: str,
        repo: str,
        branch: str,
        file: str
):
    pass

def async_get_version(
        user: str,
        repo: str,
        branch: str,
        file: str
):
    pass
