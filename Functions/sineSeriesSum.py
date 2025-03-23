

# --- Find the Sum of Sine Series --- !

import math

def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n - 1)

def sine_series(x, terms):

	sine_sum = 0
	for i in range(terms):
		power = 2 * i + 1
		sign = (-1) ** i
		term = sign * (x ** power) / factorial(power)
		sine_sum += term
	return sine_sum

angle_degrees = float(input("Enter the angle in degrees: "))
terms = int(input("Enter the number of terms: "))
# angle_degrees = 90
# terms = 5

angle_radians = math.radians(angle_degrees)

sine_sum = sine_series(angle_radians, terms)

print(f"The Sum of the Sine Series for {angle_degrees}° is :{sine_sum}")