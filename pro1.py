# Python program to design a simple calculator with basic arithmetic operators
def add(n1, n2): #For addition of two numbers
    return n1+n2

def subtract(n1, n2): #For subtraction of two numbers
    return n1-n2

def multiply(n1, n2): #For multiplciation of two numbers
    return n1*n2

def division(n1, n2): #For dividing two numbers
    return n1/n2

print("Please select operation -\n"\
        "1 Add\n"\
        "2 Subtract\n"\
        "3 Multiply\n"\
        "4 Division\n")

# Take input from the user
select=int(input("Select operations from 1, 2, 3, 4: "))
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if select == 1:
    print(num1,"+",num2,"=",add(num1, num2))
elif select == 2:
    print(num1,"-",num2,"=",subtract(num1, num2))
elif select == 3:
    print(num1,"*",num2,"=",multiply(num1, num2))
elif select == 4:
    print(num1,"/",num2,"=",division(num1, num2))
else:
    print("Invalid Input!") 