# Python Function

# What is a function in Python?

# Block of code that its defined once and can be executed as many times as needed.

# Functions are the building blocks of any programming language.

# We've already used some built-in functions like print(), input(), len(), etc.


# # Defining a function
# def greeting():
#     print("Hello there!")

# # Calling a function
# greeting()
# greeting()
# greeting()
# greeting()
# greeting()


# def print_greeting():
#     # Your code goes here. Remember to indent!
#     python_is_fun = True
#     if python_is_fun:
#         print("Python is fun!")

# # Call the function
# print_greeting()

# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    
    if letter.isalpha():
        if letter in vowels:
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonate.")
    else:
        print("Please enter a valid alphabetical character")
# Call the function
# check_letter()

# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Invalid Age")
        elif age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")
    except ValueError:
        print("Please enter a valid number representing the age")


# Call the function
# check_voting_eligibility()

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = int(input("Input a dog's age: "))
    if dog_age <= 0:
        print("Invalid age")
    elif dog_age == 1:
        print("The dog's age in dog years is 10.")
    elif dog_age == 2:
        print("The dog's age in dog years is 20.")
    else:
        print(f"The dog's age in dog years is {20 + (dog_age - 2) * 7}.")

# Call the function
# calculate_dog_years()

# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold = input("Is it cold? (yes/no): ").lower()
    rain = input("Is is raining? (yes/no): ").lower()

    if cold == "yes" and rain == "yes":
        print("Wear a weatherproof coat.")
    elif cold == "yes" and rain == "no":
        print("Wear a warm coat.")
    elif cold == "no" and rain == "yes":
        print("Carry an umbrella")
    else:
        print("Wear light clothing")

# Call the function
# weather_advice()

# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()

    if month not in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
        print("Invalid Month")
        return # this exits the function immediately
    
    
    try:
        day = int(input("Enter the day of the month: "))
        if day > 31 or day < 0:
            print("Please enter a day between 1-31")
            return
        
    except ValueError:
        print("Invalid Day")
        return # this exits the function immediately

    season = None

    # Winter
    if (month in ["Dec", "Jan", "Feb", "Mar"] and (month == "Dec" and day >= 21) or (month in ["Jan", "Feb"]) or (month == "Mar" and day <= 19)):
        season = "Winter"
    # Spring
    if (month in ["Mar", "Apr", "May", "Jun"] and (month == "Mar" and day >= 20) or (month in ["Apr", "May"]) or (month == "Jun" and day <= 20)):
        season = "Spring"
    # Summer
    if (month in ["Jun", "Jul", "Aug", "Sep"] and (month == "Jun" and day >= 21) or (month in ["Jul", "Aug"]) or (month == "Sep" and day <= 21)):
        season = "Summer"
    # Fall
    if (month in ["Sep", "Oct", "Nov", "Dec"] and (month == "Sep" and day >= 22) or (month in ["Oct", "Nov"]) or (month == "Dec" and day <= 20)):
        season = "Fall"
    
    
    print(f"{month} {day} is in {season}")


# Call the function
determine_season()


