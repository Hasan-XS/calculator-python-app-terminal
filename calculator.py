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
| plus = +                                          | 
| minus = -                                         |
| times = *                                         |
| division = %                                      |   
|___________________________________________________|
"""

description_plus = """
 ___________________________________________________
|                   OPERATION: PLUS                 |
|           Your chosen operation is plus!          |  
|___________________________________________________|
"""


description_minus = """
 ___________________________________________________
|                   OPERATION: MINUS                |
|           Your chosen operation is minus!         |  
|___________________________________________________|
"""


description_times = """
 ___________________________________________________
|                   OPERATION: TIMES                |
|           Your chosen operation is times!         |  
|___________________________________________________|
"""

description_division = """
 ___________________________________________________
|                   OPERATION: DIVISION             |
|           Your chosen operation is division!      |  
|___________________________________________________|
"""

# plus
def plus(x, y):
        plus = int(x + y)
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} + {j} = {plus}"
        print(f"Anwser:",z)


# minus
def minus(x, y):
        minus = x - y
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} - {j} = {minus}"
        print(f"Anwser:",z)


# times
def times(x, y):
        times = x * y
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} * {j} = {times}"
        print(f"Anwser:",z)


# division
def division(x, y):
        division = x % y
        for i in str(x):
            i = x
            for j in str(y):
                j = y
                z = f"{i} % {j} = {division}"
        print(f"Anwser:",z)


# Check user input
def check_input(user_input):
    if user_input == "plus":
         sleep(1)
         print(description_plus)
         number_x = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         sleep(0.5)
         plus(number_x, number_y)

    elif user_input == "minus":
         sleep(1)
         print(description_minus)
         sleep(1)
         number_x = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         sleep(0.5)
         minus(number_x, number_y)

    elif user_input == "times":
         sleep(1)
         print(description_times)
         sleep(1)
         number_x = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         sleep(0.5)
         times(number_x, number_y)
         

    elif user_input == "division":
         sleep(1)
         print(description_division)
         sleep(1)
         number_x = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
         |         Enter: """))
         print("""         ------------------------------""")
         
         
         number_y = int(input("""
          ____________________________
         |                            |
         | Please enter the number:   |
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