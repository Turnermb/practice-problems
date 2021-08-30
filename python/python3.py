# 20210720

# Lesson 1: Installing Python

# import math
# print("My first python program.")  ## Prints "My first python program."
# print(5 + 5)  ## Prints the result of 5 + 5

# Lesson 2: Statements

# Program that calculates the average of 2 numbers
# print("This program calculates the average of two numbers.")
# print("The numbers are 4 and 8")
# print("The average is: ", (4 + 8) / 2)

# Lesson 3: Variables

# age = 29
# print(age)
# print("I'm ", age, " years old.")

# Variable names can contain letters numbers and underscores.
# Variable names can't start with numbers.
# Variable names are case sensitive.
# Reserved words can't be used.

# number1 = 4
# number2 = 8
# print("The average is: ", (number1 + number2) / 2)

# Lesson 4: Input Function

# number1 = input("Please enter the first number.")
# number2 = input("Please input the second number.")
# print(number1 + number2)

# first_name = "Matthew"
# last_name = "Turner"

# print("Your e-mail address is: ", first_name + "." + last_name + "@gmail.com")

# float(number1) + float(number2)

# number1 = float(input("Please enter the first number."))
# number2 = float(input("Please input the second number."))
# print("The numbers are ", number1, " and ", number2)
# print("The average is: ", (number1 + number2) / 2)

# Lesson 5: Code Challenge
# Convert user inputted number of kilometers to miles.

# kilometers = float(input("Enter number of kilometers: "))
# miles = kilometers / 1.609344
# print(kilometers, "km is equal to", round(miles, 4), "miles.")

# Lesson 6: Data Type: Strings

# A string is a sequence of characters
# my_string = "Some text"
# type(my_string)

# Numbers can be stored in a string
# Good for numbers that are not used for calculations
# my_string = "33"
# type(my_string)

# "" and '' are usable in the same string
# my_string = 'She said "Meet me at 5."'

# Every character in a string has its own index starting from 0
# index can be retrieved using braces
# my_string[0]
# Can start from the end of the string using negative numbers
# my_string[-1]

# Every string has a length
# Can be accessed with the len() function
# len(my_string)
# Can also get the last character using len()
# my_string[len(my_string)-1]

# The slice method can be used to retrieve specified indexes
# my_string = "US1024107"
# my_string[0:2]  # Returns from index 0 until index 2
# my_string[-2:]  # Returns from index -2 until the end of the string
# my_string[:3]  # Returns from the beginning of the string until index 3

# Strings can be concatinated(?) together.
# print("Hello" + " " + "World")
# Beware of using different data types.
# Data that isn't a string can be stringified with str()
# print("user" + str(22))

# Lesson 7: String Exercises
# Create a program that asks the user for his first name, his middle name and his last name. then print: "Your initials are _ _ _."

# first_name = input("What is your first name? ")
# middle_name = input("What is your middle name? ")
# last_name = input("What is your last name? ")

# print("Your initials are " +
# first_name[0] + middle_name[0] + last_name[0] + ".")

# Let's say your company has a product with this lot number: "037-00901-00027". 037 is the country code. 00901 is the product code and 00027 is the batch number. Create a program to print: "Country Code: _ _ _. Product Code: _ _ _ _ _. Batch Number: _ _ _ _ _."

# lot_number = "037-00901-0027"

# print("Country Code: " + lot_number[:3])
# print("Product Code: " + lot_number[4:9])
# print("Batch Number: " + lot_number[10:])

# Lesson 8: Data Type: Numbers

# There are two data types to represent numbers float and integer

# num1 = 5  # Integers don't have decimals
# num2 = 102931.60  # Floats do have decimals

# addition(+), subtraction(-), multiplication(*), division(/), modulus(%), power of(**)
# Round can be used to round numbers
# round(4.88725)  # 5
# Round can take a number as an arument for number of decimal points
# round(4.88725, 2)  # 4.88

# Math module can be imported to extend functionality
# math.factorial(5)  # 5 * 4 * 3 * 2

# Can round number up or down using ceil() or floor()
# math.ceil(2.2)  # Always rounds up
# math.floor(2.8)  # Always rounds down

# Lesson 9: Number Exercises
# Create a program to calculate the area and circumference of a circle. Ask the user for the radius.math

# r = float(input("What is the radius of the circle? "))
# area = math.pi * (r**2)
# circumference = 2 * math.pi * r

# print("The area is: " + str(round(area, 2)))
# print("The circumference is: " + str(round(circumference, 2)))

# 20210826

# Lesson 10: Lists and Tuples

# Lists
# students = "John, Mary, Steve"  # string
# students = ["John", "Mary", "Steve"]  # list

# len() function returns number of students in list
# Students[0] will pull first student in list
# Can have lists of lists
# students[-1]  ## Last student
# students[:2]  ## First two students
# students[0] = "George"  ## Changes first student to George
# students.append("Juan")  ## Adds Juan to the end of the list of students
# students.insert(0, "Kate")  ## Inserts Kate at position 0
# students.pop(1)  ## Pops last student by default, but can be given an index
# students2 = ["Bill", "Doug"]

# students + students2  ## combines the two lists

# Tuples
# month = ("January", "February", "March")

# Tuples cannot be changed

# Lesson 11: Lists and Tuples Exercise

# Create a program that asks the user for his birthday in the format "DD-MM-YYYY" then print: "You were born in [month]."

# months = ("January", "February", "March", "April", "May", "June",
#           "July", "August", "September", "October", "November", "December")

# birthday = input("What is your birthday? (DD-MM-YYYY) ")
# index = int(birthday[3:5]) - 1
# birth_month = months[index]
# print("You were born in ", birth_month)

# Create a program with a predefined list of people. Ask the user for his name, add it to the end of the list then print the updated list.

# people_list = ["Don", "Martha", "Stephen", "Cassandra", "Siegfried"]


# def list_people():
#     name = input("What is your name? ")
#     people_list.append(name)
#     print(people_list)


# list_people()

# Lesson 12: Dictionaries

# person = ["John", "Green", "1980", "Canada"]
# person = {
#     "first_name": "John",
#     "last_name": "Green",
#     "birth_year": 1980,
#     "country_of_birth": "Canada"
# }
# person["first_name"]  ## Calls on the key to pull the value
# person["birth_year"] = 1979  ## Calls the key to edit the value
# person["marital_status"] = "Married"  ## Adds new key value pair
# person["children"] = ["Nathalie", "Ethan"]  ## Adds multiple values to one key
# person["children"].append("Ana")  ## Appends new value to children list
# Gets the age of the person, if nothing is found returns "invalid property"
# person.get("age", "invalid property")
# person.clear()  ## Clears the person dictionary

# Lesson 13: Dictionaries Excersize

# Create a program with a predefined dictionary for a person, include the following information: name, gender, age, address and phone. Ask the user what information they want about the person and display error message if not found.

# person = {
#     "name": "Allen Coholic",
#     "gender": "M",
#     "age": "21",
#     "address": "123 Somewhere St",
#     "phone_number": "123-456-7890"
# }

# info = input("What would you like to know about this person? ").lower()
# print(person.get(info, "Not On File"))

# 20210829

# Lesson 14: Booleans

# myBoolean = True
# myBoolean = False

# num1 = 8
# num2 = 4
# num1 > num2  ## Returns True because 8 > 4
# num1 < num2  ## Returns False
# num1 == num2  ## False
# num1 != num2  ## True
# num1 = float(input("What is the first number?"))
# num2 = float(input("What is the second number?"))

# if (num1 > num2):
#     print(num1, "is greater than", num2)
# elif (num1 == num2):
#     print(num1, "is equal to", num2)
# else:
#     print(num1, "is less than", num2)

# print("This is out of the if structure")

# Lesson 15: Boolean Exersize

# Create a program and store your age in a variable. Then, ask the user for his age and print whether he's older than you, younger than you or you two have the same age

# mt_age = 29
# user_age = int(input("How old are you? "))

# if (mt_age > user_age):
#     print("Congratulations, you are younger than me.")
# elif (mt_age == user_age):
#     print("We're the same age. Getting up there.")
# else:
#     print("You are older, but with age comes wisdom.")

# 20210830

# Lesson 16: Conditionals

# grade1 = float(input("Type the grade of the first test: "))
# grade2 = float(input("Type the grade of the second test: "))
# absences = int(input("Type the number of absences: "))
# total_classes = int(input("Type the total number of classes: "))

# avg_grade = (grade1 + grade2) / 2
# attendance = (total_classes - absences) / total_classes

# print("Average Grade:", round(avg_grade, 2),
#       "Attendance:", round(attendance, 2))

# if (avg_grade >= 6):
#     if (attendance >= 0.8):
#         print("The student was approved!")
#     else:
#         print("The student has failed. Attendance lower than 80%.")
# elif (attendance >= 0.8):
#     print("The student has failed. Average grade lower than 6.")
# else:
#     print("The student has failed. Average grade lower than 6 and attendance lower than 80%.")

# Lesson 17: And/Or

# if (avg_grade >= 6 and attendance >= 0.8):
#     print("The student was approved!")
# elif (avg_grade < 6 and attendance < 0.8):
#     print("The student has failed. Average grade lower than 6 and attendance lower than 80%.")
# elif (attendance >= 0.8):
#     print("The student has failed. Average grade lower than 6.")
# else:
#     print("The student has failed. Attendance lower than 80%.")

# Lesson 18: Conditionals Exercise

# Create a program to calculate the BMI of a person. Ask the user for the height in meters and his weight in kg

## BMI = weight / (height * height)

# Print BMI and Classification

# height = float(input("What is your height in inches? "))
# weight = float(input("What is your weight in pounds? "))
# bmi = round((weight / (height * height)) * 703, 2)

# print(bmi)
# if (bmi <= 18.5):
#     print("Underweight")
# elif (bmi > 18.5 and bmi <= 24.9):
#     print("Normal Weight")
# elif (bmi > 24.9 and bmi <= 29.9):
#     print("Overweight")
# else:
#     print("Obese")
