import random
import string

character = list(string.ascii_letters) + list(string.punctuation) + list(string.digits)
password_length = int(input("Enter the length of your password:\n"))
if password_length <= len(character):
    password = random.choices(character, k = password_length)
    print("Your password is", password)
