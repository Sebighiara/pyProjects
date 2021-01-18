#The function below calculates the sum of two numbers
def sum (number1, number2):
    return number1 + number2

#the function below calculates the difference of two numbera
def difference (number1, number2):
    return number1 - number2

#the function below calculates the product of two numbers
def product (number1, number2):
    return number1 * number2

#the function below calculates a number divided by another
def division (number1, number2):
    return number1 / number2

#two variables will stock a number each other
print ("Insert 2 numbers: ")
firstNumber = int(input())
secondNumber = int(input())

#then, there will be showed some operations and one will be chosen
print ("Choose one option")
print ("1) sum")
print ("2) difference")
print ("3) multiplication")
print ("4) division")
option = input()

#and here, the operation that has been chosen above is executed
if option == "1" or option == "sum":
    result = sum (firstNumber, secondNumber)
elif option == "2" or option == "difference":
    result = difference (firstNumber, secondNumber)
elif option == "3" or option == "multiplication":
    result = product (firstNumber, secondNumber)
elif option == "4" or option == "division":
    result = division (firstNumber, secondNumber)
print (result)
