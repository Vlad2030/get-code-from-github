from get_github_code import get_code

code = get_code(
    user="Vlad2030",
    repo="get-code-from-github",
    branch="main",
    file_path="VERSION",
)

print(code)
