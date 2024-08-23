# pylint:disable=W0702
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")


def generate_password():
    password_length = int(input("how long it should be :>"))

    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))
    password = "".join(password)

    print(password)


option = input("want to generate a password? (y/n)")

if option == "y":
    generate_password()
elif option == "n":
    print("good by")
