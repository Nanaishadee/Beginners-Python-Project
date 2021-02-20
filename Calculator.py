# Basic Calculator
number_1 = input("Enter number_1 here: ")
number_2 = input("Enter number_2 here: ")
result = int(number_1) + int(number_2)
print(result)


""" Advanced Calculator Steps 
1. Get input from users (three variables) # number1, operator, number2
2. Convert the data type 
3. using if statements and else statements
4. use print
"""

num1 = int(input("Enter num1 here: "))
operator = input("Enter operator here: ")
num2 = int(input("Enter num2 here: "))
if operator == "-":
    print(num1 - num2)
elif operator == "**":
    print(num1 ** num2)
elif operator == "+":
    print(num1 + num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Sorry I do not recognize the operator ")
    
    
    
    



