import random
import string

print("================================")
print("      PASSWORD GENERATOR")
print("================================")

length = int(input("Enter password length: "))

letters = input("Include letters? (y/n): ").lower()
numbers = input("Include numbers? (y/n): ").lower()
symbols = input("Include special characters? (y/n): ").lower()

characters = ""

if letters == "y":
    characters += string.ascii_letters

if numbers == "y":
    characters += string.digits

if symbols == "y":
    characters += string.punctuation

if characters == "":
    print("Please select at least one option!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nYour generated password is:")
    print(password)

print("\nThank you for using the Password Generator!")
