
# Import random module
# Import String module
import random

# Define custom exception


class Error(Exception):
    pass


class InvalidInput(Error):
    pass


# Take an input from the user that will determine the length of the password
len_of_password = int(input("Enter the length of your password"))


# Set the lower and upper bounds for the password. Length of password cannot be < 6 or > 50
try:
    if len_of_password < 6 or len_of_password > 50:
