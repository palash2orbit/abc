# import math
# import os
# # print(math.factorial(50000))
# os.system('cls')


# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero"
#     return x / y

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# while True:
#     opration = int(input("Enter choice (1/2/3/4): "))

#     # if opration in ('1 add', '2 subtract', '3 multiply', '4 divide'):
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if opration == 1:
#         print("Result:", add(num1,num2))
#     elif opration == 2:
#             print("Result:", subtract(num1,num2))
#     elif opration == 3:
#             print("Result:", multiply(num1,num2))
#     elif opration == 4:
#             print("Result:", divide(num1,num2))
#     else:
#         print("Invalid input")

#     another_calculation = input("Do you want to perform another calculation? (yes/no): ")
#     if another_calculation.lower() != "yes":
#         break
#######################################################################
import math

num1 =int(input('enter your value:'))
num2 =int(input('enter your value:'))

oprator=int(input("enter chose 1/add,2/subtract,3/multiply,4/divide,5/exponentiation,6/floor division,7/square root"))
if (oprator== 1):
    print ((num1+num2))
 
elif (oprator == 2):
    print (num1-num2)

elif (oprator == 3):
    print (num1*num2)

elif (oprator == 4):
    print(num1/num2)

elif (oprator == 5):
    print(num1**num2)

elif (oprator == 6):
    print(num1//num2)

elif (oprator == 7):
    sq = int(input("which sqrt do you want to perform: 1/num1, 2/num2: "))
    if(sq == 1):
        print(math.sqrt(num1))
    else:
        print(math.sqrt(num2))  

else:
    print("invaled input")
    



