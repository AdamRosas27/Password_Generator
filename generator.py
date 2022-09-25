
# Import random module
# Import String module
import random
import string

while True:
    password_len = int(input("\nDesired Password Length: "))
    if password_len < 6:
        print("Sorry, passwords cannot be less than 6 characters in length.")
    elif password_len > 50:
        print("Sorry, passwords cannot be more than 50 characters in length.")
