#importing modules
import sys


#defining funtions
def arithmetic():
    global output
    global not_valid
    n_one = input("what is the first number?: ")
    n_two = input("what is the second number?: ")
    print ("which operation should be used?:")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Exponent")
    print ("0) Back")
    math_op = input ()
    math_op.lower()
    if math_op == "add" or math_op == "addition":
        math_op = 1
    elif math_op == "subtract" or math_op == "SUBTRACTION":
        math_op = 2
    elif math_op == "multiply" or math_op == "multiplication":
        math_op = 3
    elif math_op == "divide" or math_op == "division":
        math_op = 4
    elif math_op == "exponent" or math_op == "exponentiation":
        math_op = 5

    try:
        int(n_one) and int(n_two)
        not_valid = 0
    except ValueError:
        output = ("Non vaild input.")
    if int(math_op) == (1, 5):
        output = ("Non vaild input.")
        print (output)
    else:
        if int(math_op) == (0):
            output = ("")
            print (output)
        elif not_valid == 0:
            math_operation(math_op, n_one, n_two)

def math_operation(math_op, n_one, n_two):
    if int(math_op) == 1:
        output = (f"{float(n_one)} + {float(n_two)} = {float(n_one) + float(n_two)}")
    elif int(math_op) == 2:
        output = (f"{float(n_one)} - {float(n_two)} = {float(n_one) - float(n_two)}")
    elif int(math_op) == 3:
        output = (f"{float(n_one)} * {float(n_two)} = {float(n_one) * float(n_two)}")
    elif int(math_op) == 4:
        output = (f"{float(n_one)} / {float(n_two)} = {float(n_one) / float(n_two)}")
    elif int(math_op) == 5:
        output = (f"{float(n_one)}^{float(n_two)} = {float(n_one) ** float(n_two)}")
    print (output)






def varible_editor():
    print("What would you like to do?:")
    print("1)Varible creator")
    print("2)Varible editor")
    print("3)Varible observer")
    print("0)Back")
    var_edit_select = input()
    var_edit_select.lower()
    
    
    try:
        int(var_edit_select)
        not_valid = 0
    except ValueError:
        not_valid = 1
    
    if not_valid == 1:
        print(invalid)

def calc_funtion():
    if int(calc_option) == 1:
        arithmetic()
    elif int(calc_option) == 2:
        varible_editor()
    
    elif int(calc_option) == 0:
        print("Exiting calculator")
        sys.exit()

#defining global varibles
invalid = ("Non vaild input.")
math_op = -1
calc_option = -7
x = 1
math_op = 0

#start of acual code

while True: 
    not_valid = 0
    if calc_option == 0:
        x = 1
    else:
        x = 1
    print("What would you like to do?")
    print("1) Arithmetic")
    print("2) Varible editor")
    print("0) Exit")
    calc_option = input()
    try:
        int(calc_option)
        calc_valid = 1
    except ValueError:
        calc_valid = 0
    if calc_valid == 0:
        print (invalid)
    else:
        calc_funtion()
    
