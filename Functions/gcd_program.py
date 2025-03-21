def find_gcd(a,b):
	while b:
		a, b = b, a % b
	return a

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Secend Number: "))

gcd = find_gcd(num1, num2)

print(f"The GCD os {num1} and {num2} is {gcd}")