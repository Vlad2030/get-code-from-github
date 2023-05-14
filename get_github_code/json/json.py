import typing

import orjson


class JSON:
    def __init__(self) -> None:
        pass

    @staticmethod
    def loads(
            self,
            data: typing.Union[bytes, bytearray, memoryview, str],
    ) -> typing.Any:
        return orjson.loads(data)
