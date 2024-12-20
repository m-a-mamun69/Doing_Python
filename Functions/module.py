# Python Modules
# import math
# import math as m   # Rename Module
import calculator
from math import sqrt, pi, sin      # (* Means all) Using From import statement 

num = 49
value = sin(pi/2)
result = sqrt(num)
print(f"{num} Square root is: {result}")
print(f"PI Number: {pi}")
print(f"Value is: {value}")

result1 = calculator.add(4,5)
print(f"Addition: {result1}")

result2 = calculator.subtract(10,5)
print(f"Subtractions: {result2}")

result3 = calculator.multiply(4,5)
print(f"Multipications: {result3}")

result4 = calculator.divide(20,5)
print(f"Division: {result4}")