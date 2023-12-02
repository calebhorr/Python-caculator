def arithmetic():
    first_number = input ("what is the first number?: ")
    second_number = input ("what is the second number?: ")
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
    if math_op == "subtract" or math_op == "SUBTRACTION":
        math_op = 2
    if math_op == "multiply" or math_op == "multiplication":
        math_op = 3
    if math_op == "divide" or math_op == "division":
        math_op = 4
    if math_op == "exponent" or math_op == "exponentiation":
        math_op = 5

    try:
        float(first_number) and float(second_number)
        not_valid = 0
    except ValueError:
        not_valid = 1
    if int(math_op) == (0):
       output = ("")
    else:
        if int(math_op) != (1, 5):
            output = ("Non vaild input.")
        if not_valid == 1:
            output = ("Non vaild input.")
        else:
            if int(math_op) == 1:
                output = (f"{float(first_number)} + {float(second_number)} = {float(first_number) + float(second_number)}")
            if int(math_op) == 2:
                output = (f"{float(first_number)} - {float(second_number)} = {float(first_number) - float(second_number)}")
            if int(math_op) == 3:
                output = (f"{float(first_number)} * {float(second_number)} = {float(first_number) * float(second_number)}")
            if int(math_op) == 4:
                output = (f"{float(first_number)} / {float(second_number)} = {float(first_number) / float(second_number)}")
            if int(math_op) == 5:
                output = (f"{float(first_number)}^{float(second_number)} = {float(first_number) ** float(second_number)}")
                
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
    
    

#start of acual code
invalid = ("Non vaild input.")
math_op = -1
calc_option = -1
x = 1
while True: 
    not_valid = 0
    if calc_option == 0:
        x = 1
    else:
        x = 1
    print("What would you like to do?")
    print("1) Arithmetic")
    print("2) Varible editor")
    """calc_option = int(input())
    try:
        int(calc_option)
        calc_valid = 1
    except ValueError:
        calc_valid = 0
    if calc_valid == 0:
        print (invalid)"""
    
        

    
    arithmetic()
    
