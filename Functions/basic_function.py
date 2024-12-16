# def function_name(parameters):
#     # Code block or logic
#     return value


# Greeting Using Function.

def greet():
    print("Hi, Python Lovers!")

#Call the Function
greet()

# Adding parameter to a Function.
def greet_user(name):
    print(f"Hello, {name}")

#Call the Function
greet_user("Rashid")
greet_user("Rony")


# Returning Value Using Return Keyword
def add_numbers(numberOne, numberTwo):
    return numberOne + numberTwo

#Call the Function
result = add_numbers(50, 60)
print(f"The Sum is: {result}")