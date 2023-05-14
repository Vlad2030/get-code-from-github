from get_github_code import GetCode, get_code

code = get_code(
    user="Vlad2030",
    repo="get-code-from-github",
    branch="main",
    file_path="VERSION",
)
print(code)
# 0.2

file = GetCode(
    user="Vlad2030",
    repo="get-code-from-github",
    branch="main",
    file_path="VERSION",
)
print(file.get_code)
# 0.2