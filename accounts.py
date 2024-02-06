# Week3 Task - Aim is to input a 10 digit number and for the output to be the last 4 digits and X's

#Create Variable - Requesting a 10 digit number
account_number = input("Please enter an 10 digit account number")

# Printing 6 X's representing the first 6 numbers of the account number
# Converting the account number to a string to we can concat
# Using slicing to produce the last 4 digits of the input
print("Your account number is  XXXXXX" + str(account_number[-4:]))

