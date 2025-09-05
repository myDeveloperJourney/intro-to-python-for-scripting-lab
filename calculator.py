# Write a script that prompts the user to enter two numbers and an operator (+, -, *, /).

print("Welcome to the Python Calculator!")
num1 = int(input("Enter the first number: "))
operator = input("Please enter an operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

result = None

# Use conditional statements (if, elif, else) to determine the operation based on the user’s input.
# Perform the corresponding arithmetic operation.
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 // num2
else:
    print("Invalid Operator")

print(result)



# Display the result of the operation to the user.

# Run the script to confirm it does what you want it to!