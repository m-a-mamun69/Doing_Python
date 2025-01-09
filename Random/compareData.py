# Compare Sensitive Data Securely
import secrets
actual_token = input("Enter Actual Token: ")
user_token = input("Enter User Token: ")

if secrets.compare_digest(actual_token, user_token):
    print("Tokens Match.")
else:
    print("Token do not match.")
    