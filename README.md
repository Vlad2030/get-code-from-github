## Get code from GitHub
this is a small python code to get code from github repositories

## Usage
```python
from get_github_code import get_code

code = get_code(
    user="Vlad2030",
    repo="get-code-from-github",
    branch="main",
    file_path="get_github_code.py",
)

print(code)
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
        file_path="get_github_code.py",
    )

    print(code)

if __name__ == "__main__":
    asyncio.run(main())
```
