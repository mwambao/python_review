

num1 = input("Please enter first number: ")
num2 = input("Please enter second number: ")
num3 = input("Please enter third number: ")

def maxNum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


result = maxNum(num1,num2,num3)

print(f"The max number is {result}")