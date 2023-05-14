import base64


class Decode:
    def __init__(self) -> None:
        pass

    @staticmethod
    def b64(
            data: str,
            decode_type: str = "utf-8",
            *args,
            **kwargs,
    ) -> str:
        return (base64.b64decode(s=data, *args, **kwargs)
                      .decode(decode_type, *args, **kwargs))
