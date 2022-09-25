
# Import random module
# Import String module
import random

# Define custom exception


class Error(Exception):
    pass


class InvalidInput(Error):
    pass


# Set the lower and upper bounds for the password. Length of password cannot be < 6 or > 50
while True:
    len_of_password = int(input("\nDesired Password Length:"))
try:
    if len_of_password < 6 or len_of_password > 50:
        raise InvalidInput
except InvalidInput:

    print("\nThe length of the password cannot be less than 6 characters of greater than 50 characters.")
