from get_github_code.constants import API_URL
from get_github_code.decode import Decode
from get_github_code.exceptions import GetCodeException
from get_github_code.json import JSON
from get_github_code.request import Request


class GetCode(Request, JSON, Decode):
    """### GetCode class

        Args:
            `user (str)`: GitHub Username

            `repo (str)`: GitHub repository name

            `branch (str)`: Github repository branch

            `file_path (str)`: File path in repository

        functions:
            `(property) get_code -> str:`
                Return github code from file_path

            `(property) async_get_code -> str:`
                Asynchronous return github code from file_path
    """
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
        """Return github code from file_path"""

        response = self.request(url=self.url)
        if not response.status == 200:
            raise GetCodeException("Connection refused")
        return self.loads(data=response._body.decode("utf-8"))["content"]

    @property
    async def async_get_code(self) -> str:
        """Asynchronous return github code from file_path"""

        response = await self.async_request(url=self.url)
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
    """Get github code from repository

        Args:
            `user (str)`: GitHub Username

            `repo (str)`: GitHub repository name

            `branch (str)`: Github repository branch. Defaults to `"main"`

            `file_path (str)`: File path in repository

    Returns:
        str: Code from github repository
    """
    return GetCode(user, repo, branch, file_path).get_code


async def async_get_code(
        user: str,
        repo: str,
        file_path: str,
        branch: str = "main",
) -> str:
    """Asynchronous get github code from repository

        Args:
            `user (str)`: GitHub Username

            `repo (str)`: GitHub repository name

            `branch (str)`: Github repository branch. Defaults to `"main"`

            `file_path (str)`: File path in repository

    Returns:
        str: Code from github repository
    """
    return await GetCode(user, repo, branch, file_path).async_get_code
