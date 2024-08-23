import re

EMAIL_REGEX = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
MIN_EMAIL_LENGTH = 12


def is_valid_email(email):
    if len(email) < MIN_EMAIL_LENGTH:
        return False, "Email is too short"

    if not re.match(EMAIL_REGEX, email):
        return False, "Invalid email format"

    if any(char.isupper() for char in email):
        return False, "Email should not contain uppercase letters"

    if " " in email:
        return False, "Email should not contain spaces"

    return True, "Valid email"


def main():
    email = input("Enter your email: ")
    is_valid, message = is_valid_email(email)
    print(message)


if __name__ == "__main__":
    main()
