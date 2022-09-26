
# Import random module
# Import String module
from lib2to3.pygram import Symbols
import random
import string

import symbol

while True:
    password_len = int(input("\nDesired Password Length: "))
    if password_len < 6:
        print("\nSorry, passwords cannot be less than 6 characters in length. Try again.")
    elif password_len > 50:
        print("\nSorry, passwords cannot be more than 50 characters in length. Try again.")
    else:
        break

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
special_chars = string.punctuation
