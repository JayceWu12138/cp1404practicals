def extract_name(email):
    parts = email.split('@')[0]
    parts = parts.replace('.', ' ').replace('_', ' ')
    name = parts.title()
    return name


def get_name_from_email():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation not in ('y', 'yes', ''):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    return email_to_name


def print_email_directory(email_to_name):
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def main():
    email_to_name = get_name_from_email()
    print_email_directory(email_to_name)


if __name__ == "__main__":
    main()
