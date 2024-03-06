from time import sleep

# calculator app terminal
# Created By SMART


# Description For User Display 
description_app = """
                Calculator By Smart
 ___________________________________________________
|                                                   |
| Hello My Friend!, welcome to my terminal program, |\n| nthis is a calculator program, here you can do    |\n| 4 operations! which one do you want to do? :      |
|                                                   |
| Addition = +                                      | 
| Subtraction = -                                   |
| Multiplication = *                                |
| Division = %                                      |   
|___________________________________________________|
"""

description_addition = """
 ___________________________________________________
|                   OPERATION: ADDITION             |
|           Your chosen operation is addition!      |  
|___________________________________________________|
"""


description_subtraction = """
 ___________________________________________________
|               OPERATION: SUBTRACTION              |
|         Your chosen operation is subtraction!     |  
|___________________________________________________|
"""


description_multiplication = """
 ___________________________________________________
|             OPERATION: MULTIPLICATION             |
|      Your chosen operation is Multiplication!     |  
|___________________________________________________|
"""

description_division = """
 ___________________________________________________
|                   OPERATION: DIVISION             |
|           Your chosen operation is division!      |  
|___________________________________________________|
"""

# addition
def addition(x, y):
        addition = int(x + y)
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} + {j} = {addition}"
        print(f"Anwser:",z)


# subtraction
def subtraction(x, y):
        subtraction = x - y
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} - {j} = {subtraction}"
        print(f"Anwser:",z)


# multiplication
def multiplication(x, y):
        multiplication = x * y
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} * {j} = {multiplication}"
        print(f"Anwser:",z)


# division
def division(x, y):
        division = x / y
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} / {j} = {division}"
        print(f"Anwser:",z)


# Check user input
def check_input(user_input):
    if user_input == "addition":
         sleep(1)
         print(description_addition)
         number_x = int(input("""
          ____________________________
         |                            |
         | Enter your first number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Enter your second number:  |
         |         Enter: """))
         print("""         ------------------------------""")
         sleep(0.5)
         addition(number_x, number_y)

    elif user_input == "subtraction":
         sleep(1)
         print(description_subtraction)
         sleep(1)
         number_x = int(input("""
          ____________________________
         |                            |
         | Enter your first number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Enter your second number:  |
         |         Enter: """))
         print("""         ------------------------------""")
         sleep(0.5)
         subtraction(number_x, number_y)

    elif user_input == "multiplication":
         sleep(1)
         print(description_multiplication)
         sleep(1)
         number_x = int(input("""
          ____________________________
         |                            |
         | Enter your first number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Enter your second number:  |
         |         Enter: """))
         print("""         ------------------------------""")
         sleep(0.5)
         multiplication(number_x, number_y)
         
    elif user_input == "division":
         sleep(1)
         print(description_division)
         sleep(1)
         number_x = int(input("""
          ____________________________
         |                            |
         | Enter your first number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Enter your second number:  |
         |         Enter: """))
         print("""         ------------------------------""")
         sleep(0.5)
         division(number_x, number_y)

# input user
print(description_app)
while True:
    user_input = input("What operation do you want to do?, According to the options above👆: ")
    check_input(user_input)
    if user_input == "q":
         break