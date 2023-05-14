from get_github_code.json import JSON
from get_github_code.get_code import GetCode
from get_github_code.constants import API_URL
from get_github_code.decode import Decode
from get_github_code.exceptions import GetCodeException
from get_github_code.request import Request

__all__ = [
    "JSON",
    "API_URL",
    "Decode",
    "GetCodeException",
    "GetCode",
    "Request",
]

def get_version(
        user: str,
        repo: str,
        file: str,
        branch: str = "main",
) -> str:
    return GetCode(user, repo, branch, file).get_version

async def async_get_version(
        user: str,
        repo: str,
        file: str,
        branch: str = "main",
):
    return await GetCode(user, repo, branch, file).async_get_version