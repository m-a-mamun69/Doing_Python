# Generate a Secure Random Integer
import secrets

random_number = secrets.randbelow(100) + 1
print("Random Number: ", random_number)