RESTRICT = 5


def main():
    print("Please enter your password:")
    password = input("> ")
    if len(password) < RESTRICT:
        print("Password is too short")
    else:
        print('*' * len(password))


main()
