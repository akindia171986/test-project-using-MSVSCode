from datetime import date
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

# a = 3
# type(3)
# print (a)

# date.today()
# print ("Today's date is: " + str(date.today()))

# print("Welcome to the great program")
# name = input("Enter your name: ")
# print("Greetings "+ name)

# print("Calculator program")
# first_number=input("first number: ")
# second_number=input("second number: ")
# print("Total is: " + (str(int(first_number)) + str(int(second_number))))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")