
# Import random module
# Import String module
import random
import string

# Loop that continues if the given input is invalid
while True:
    # Password variable that is set to the user input
    password_len = int(input("\nDesired Password Length: "))
    # Check to see if given input is a valid length
    if password_len < 6:
        print("\nSorry, passwords cannot be less than 6 characters in length. Try again.")
    elif password_len > 50:
        print("\nSorry, passwords cannot be more than 50 characters in length. Try again.")
    else:
        # Print the length of the password the user chose to confirm
        print("You chose a password of length: " + str(password_len))
        break

# Add variables
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
special_chars = string.punctuation

# Combine variables into one string and randomize them
combined = lower_case + upper_case + numbers + special_chars
temp_pw = random.sample(combined, password_len)
password = "".join(temp_pw)
# Print the final product and display it to user
print("Your generated password is: {}".format(password))
