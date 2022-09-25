
# Import random module
# Import String module
import random
import string

while True:
    password_len = int(input("\nDesired Password Length: "))
    if password_len < 6 or password_len > 50:
