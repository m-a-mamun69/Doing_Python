# --- Calculate the power Using Recursion --- !

def  power(base, exp):
	if exp == 0:
		return 1
	return base * power(base, exp - 1)

base = int(input("Enter the Base Number: "))
exp = int(input("Enter the Exponent Number: "))

result = power(base, exp)
print("Result: ", result)