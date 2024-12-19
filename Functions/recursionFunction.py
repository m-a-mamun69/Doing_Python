# Recursive Function
def factorial(x):

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
#Function Call
num = int(input("Enter The Number: "))
print(f"The Factorial of {num} is : {factorial(num)}")