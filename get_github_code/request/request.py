import typing

import aiohttp
import urllib3


class Request:
    def __init__(self, method: str = "GET") -> None:
        self.method = method

    def request(
            self,
            url: str,
            headers: dict = None,
            *args,
            **kwargs
    ) -> typing.Any:
        http = urllib3.PoolManager()
        return http.request(method=self.method, url=url,
                            headers=headers, *args, **kwargs)

    async def async_request(
            self,
            url: str,
            headers: dict = None,
            *args,
            **kwargs,
    ) -> typing.Any:
        async with aiohttp.ClientSession(headers=headers) as http:
            return await http.request(method=self.method,
                                      url=url, *args, **kwargs)
