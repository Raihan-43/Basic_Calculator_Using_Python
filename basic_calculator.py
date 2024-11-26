#this is a basic calculator that can perform
#addition, subtraction,divission, multipliction
print(""" \n          This is a simple calculator.
           It can do sevaral things.
           --> select 1 for Addition
           --> select 2 for Subtraction
           --> select 3 for Division
           --> select 4 for Multiplication""")

def add_two_numbers(num1, num2):
    print("\n Performing --> Addition\n1")
    result= num1 + num2
    print(f"Result = {result}")

def subtract_two_numbers(num1, num2):
    print("\n Performing --> Subtraction\n")
    result= num1 - num2
    print(f"Result = {result}")

def divide_two_numbers(num1, num2):
    print("\n Performing --> Division\n")
    result= num1 / num2
    print(f"Results = {result}")

def multiply_two_numbers(num1, num2):
    print("\n Performing --> Multiplication\n")
    result= num1 * num2
    print(f"Result = {result}")

active= True
while active:
    print("\nEnter 'quit' anytime to exit the program.")
    mode= input("\nWhat operation do you want to perform: ")
    if mode == 'quit':
        active= False
        break
    elif mode != '1' and mode != '2' and mode != '3' and mode != '4':
        print("Not a valid input for mode selection.\n Enter any number between 1 and 4.")
        continue
    try:    
        num_1= int(input("Enter the first number: "))
    except ValueError:
        print("Not a valid input. Please enter a Number")
        continue
    if num_1 == 'quit':
        active= False
        break

    try:
        num_2= int(input("Enter the 2nd number: "))
    except ValueError:
        print("Not a valid input. Please enter a Number")
        continue

    if num_2 == 'quit':
        active= False
        break

    if mode == '1':
        add_two_numbers(num_1, num_2)
    
    elif mode == '2':
        subtract_two_numbers(num_1, num_2)
    
    elif mode == '3':
        divide_two_numbers(num_1, num_2)
    
    elif mode == '4':
        multiply_two_numbers(num_1, num_2)
    

    

