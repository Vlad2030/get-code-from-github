import asyncio

from get_github_code import GetCode, async_get_code


async def main() -> None:
    code = await async_get_code(
        user="Vlad2030",
        repo="get-code-from-github",
        branch="main",
        file_path="VERSION",
    )
    print(code)

    file = GetCode(
        user="Vlad2030",
        repo="get-code-from-github",
        branch="main",
        file_path="VERSION",
    )
    print(file.async_get_code)

asyncio.run(main())
# 0.2