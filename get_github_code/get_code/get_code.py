from get_github_code.constants import API_URL
from get_github_code.json import JSON
from get_github_code.decode import Decode
from get_github_code.exceptions import GetCodeException
from get_github_code.request import Request


class GetCode(Request, JSON, Decode):
    def __init__(
            self,
            user: str,
            repo: str,
            branch: str,
            file_path: str,
    ) -> None:
        self.user: str = user
        self.repo: str = repo
        self.branch: str = branch
        self.file: str = file_path
        self.url: str = API_URL.format(self.user, self.repo,
                                       self.file, self.branch)

    @property
    def get_code(self) -> str:
        response = self.request(url=self.url)._body.decode("utf-8")
        if not response.status == 200:
            raise GetCodeException("Connection refused")
        json = self.loads(data=response)["content"]
        return self.b64(data=json)

    @property
    async def async_get_code(self) -> str:
        response = await self.async_request(url=self.url)._body.decode("utf-8")
        if not response.status == 200:
            raise GetCodeException("Connection refused")
        json = self.loads(data=response)["content"]
        return self.b64(data=json)


def get_code(
        user: str,
        repo: str,
        file_path: str,
        branch: str = "main",
) -> str:
    return GetCode(user, repo, branch, file_path).get_code

async def async_get_code(
        user: str,
        repo: str,
        file_path: str,
        branch: str = "main",
):
    return await GetCode(user, repo, branch, file_path).async_get_code