import re


def password_validation():
    password = input("Enter your password:")
    if (re.search('[a-zA-Z]', password)
            and re.search('[0-9]', password)
            and len(password) in range(6, 16)
            and re.search('[$#@]', password)):
        return "Password is valid"
    else:
        return "Password is not valid"


print(password_validation())
