from get_github_code import API_URL, JSON, Decode, GetCodeException, Request


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
    def get_version(self) -> str:
        response = self.request(url=self.url)
        if not response.status == 200:
            raise GetCodeException("Connection refused")
        json = self.loads(data=response)
        return self.b64(data=json)

    @property
    async def async_get_version(self) -> str:
        response = await self.async_request(url=self.url)
        if not response.status == 200:
            raise GetCodeException("Connection refused")
        json = self.loads(data=response)
        return self.b64(data=json)