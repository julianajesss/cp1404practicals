"""
Emails
Estimate: 20 minutes
Actual:   30 minutes
"""


def main():
    """Get emails till blank, try to determine name from email, print emails and names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = determine_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")


def determine_name(email):
    """Determine a name from an email"""
    name = email.split("@")
    name = name[0]
    if "." in name:
        name = name.split(".")
        name = " ".join(name)
    return name.title()


main()
