# For Local Variable
def localTest(): #function
    # Local Variable declare
    message = "Local"
    print(f"Local Vriable: {message}")

# Function call
localTest()
# Try to call Local Variable (Error)
print(f"Global Vriable: {message}")