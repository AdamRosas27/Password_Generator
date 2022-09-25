# Define custom exception
import string
import random


class Error(Exception):
    pass


# Import random module
# Import String module

# Take an input from the user that will determine the length of the password
len_of_password = int(input("Enter the length of your password"))


# Set the lower and upper bounds for the password. Length of password cannot be < 6 or > 50
