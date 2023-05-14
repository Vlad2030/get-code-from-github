[![CodeFactor](https://www.codefactor.io/repository/github/vlad2030/get-code-from-github/badge/main)](https://www.codefactor.io/repository/github/vlad2030/get-code-from-github/overview/main)

## Get code from GitHub
this is a small python library to get code from github repositories

## How to install
```bash
pip3 install get_github_code
```

## Usage
is easy to use

```python
from get_github_code import get_code

code = get_code(
    user="Vlad2030",
    repo="get-code-from-github",
    branch="main",
    file_path="VERSION",
)

print(code)
# 0.1
```

or asynchronous

```python
import asyncio
from get_github_code import async_get_code

async def main() -> None:
    code = await async_get_code(
        user="Vlad2030",
        repo="get-code-from-github",
        branch="main",
        file_path="VERSION",
    )

    print(code)

asyncio.run(main())
# 0.1
```

additionally you can through the class by calling property

```python
import asyncio
from get_github_code import GetCode

file = GetCode(
    user="Vlad2030",
    repo="get-code-from-github",
    branch="main",
    file_path="VERSION",
)

print(file.get_code)
# 0.1

async def main() -> None:
    file = GetCode(
        user="Vlad2030",
        repo="get-code-from-github",
        branch="main",
        file_path="VERSION",
    )

    print(file.async_get_code)

asyncio.run(main())
# 0.1
```

## Documentation
[How to install](https://github.com/Vlad2030/get-code-from-github/blob/main/docs/install.md)

[Classes/GetCode](https://github.com/Vlad2030/get-code-from-github/blob/main/docs/classes/GetCode.md)

[functions/get_code](https://github.com/Vlad2030/get-code-from-github/blob/main/docs/functions/get_code.md)

[functions/async_get_code](https://github.com/Vlad2030/get-code-from-github/blob/main/docs/functions/async_get_code.md)


> 2023, version 0.0.1