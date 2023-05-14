## Get code from GitHub
this is a small python code to get code from github repositories

## Usage
```python
from get_github_code import get_code

code = get_code(
    user="Vlad2030",
    repo="get-code-from-github",
    branch="main",
    file_path="VERSION",
)

print(code)
# 0.0.1
```

or

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

if __name__ == "__main__":
    asyncio.run(main())
    # 0.0.1
```
> 2023, version 0.0.1
