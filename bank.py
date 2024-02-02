# Week2 Task - Converting two different cent values into one euro amount

# Create two variables & convert input into an integer.
# Without converting we can't perform mathematical function

amount_one = int(input("Enter amount in cents "))
amount_two = int(input("Enter second amount in cents "))

total_amount = amount_one + amount_two

# Convert to euros

euro_value = total_amount / 100

# Can only concatenate str (not "float") to str
print("€" + str(euro_value))