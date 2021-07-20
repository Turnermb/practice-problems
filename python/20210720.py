# Lesson 1: Installing Python

import math
print("My first python program.")  # Prints "My first python program."
print(5 + 5)  # Prints the result of 5 + 5

# Lesson 2: Statements

# Program that calculates the average of 2 numbers
print("This program calculates the average of two numbers.")
print("The numbers are 4 and 8")
print("The average is: ", (4 + 8) / 2)

# Lesson 3: Variables

age = 29
print(age)
print("I'm ", age, " years old.")

# Variable names can contain letters numbers and underscores.
# Variable names can't start with numbers.
# Variable names are case sensitive.
# Reserved words can't be used.

number1 = 4
number2 = 8
print("The average is: ", (number1 + number2) / 2)

# Lesson 4: Input Function

number1 = input("Please enter the first number.")
number2 = input("Please input the second number.")
print(number1 + number2)

first_name = "Matthew"
last_name = "Turner"

print("Your e-mail address is: ", first_name + "." + last_name + "@gmail.com")

float(number1) + float(number2)

number1 = float(input("Please enter the first number."))
number2 = float(input("Please input the second number."))
print("The numbers are ", number1, " and ", number2)
print("The average is: ", (number1 + number2) / 2)

# Lesson 5: Code Challenge
# Convert user inputted number of kilometers to miles.

kilometers = float(input("Enter number of kilometers: "))
miles = kilometers / 1.609344
print(kilometers, "km is equal to", round(miles, 4), "miles.")

# Lesson 6: Data Type: Strings

# A string is a sequence of characters
my_string = "Some text"
type(my_string)

# Numbers can be stored in a string
# Good for numbers that are not used for calculations
my_string = "33"
type(my_string)

# "" and '' are usable in the same string
my_string = 'She said "Meet me at 5."'

# Every character in a string has its own index starting from 0
# index can be retrieved using braces
my_string[0]
# Can start from the end of the string using negative numbers
my_string[-1]

# Every string has a length
# Can be accessed with the len() function
len(my_string)
# Can also get the last character using len()
my_string[len(my_string)-1]

# The slice method can be used to retrieve specified indexes
my_string = "US1024107"
my_string[0:2]  # Returns from index 0 until index 2
my_string[-2:]  # Returns from index -2 until the end of the string
my_string[:3]  # Returns from the beginning of the string until index 3

# Strings can be concatinated(?) together.
print("Hello" + " " + "World")
# Beware of using different data types.
# Data that isn't a string can be stringified with str()
print("user" + str(22))

# Lesson 7: String Exercises
# Create a program that asks the user for his first name, his middle name and his last name. then print: "Your initials are _ _ _."

first_name = input("What is your first name? ")
middle_name = input("What is your middle name? ")
last_name = input("What is your last name? ")

print("Your initials are " +
      first_name[0] + middle_name[0] + last_name[0] + ".")

# Let's say your company has a product with this lot number: "037-00901-00027". 037 is the country code. 00901 is the product code and 00027 is the batch number. Create a program to print: "Country Code: _ _ _. Product Code: _ _ _ _ _. Batch Number: _ _ _ _ _."

lot_number = "037-00901-0027"

print("Country Code: " + lot_number[:3])
print("Product Code: " + lot_number[4:9])
print("Batch Number: " + lot_number[10:])

# Lesson 8: Data Type: Numbers

# There are two data types to represent numbers float and integer

num1 = 5  # Integers don't have decimals
num2 = 102931.60  # Floats do have decimals

# addition(+), subtraction(-), multiplication(*), division(/), modulus(%), power of(**)
# Round can be used to round numbers
round(4.88725)  # 5
# Round can take a number as an arument for number of decimal points
round(4.88725, 2)  # 4.88

# Math module can be imported to extend functionality
math.factorial(5)  # 5 * 4 * 3 * 2

# Can round number up or down using ceil() or floor()
math.ceil(2.2)  # Always rounds up
math.floor(2.8)  # Always rounds down

# Lesson 9: Number Exercises
# Create a program to calculate the area and circumference of a circle. Ask the user for the radius.math

r = float(input("What is the radius of the circle? "))
area = math.pi * (r**2)
circumference = 2 * math.pi * r

print("The area is: " + str(round(area, 2)))
print("The circumference is: " + str(round(circumference, 2)))
