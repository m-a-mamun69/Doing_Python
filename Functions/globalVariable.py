# For Global Variable
# Global Variable declare
message = "Yes, Hello!"

def localTest(): #function define
    # Local Variable declare
    print(f"Local Vriable: {message}")

# Function call
localTest()
# Try to call Global Variable (it's Work.)
print(f"Global Vriable: {message}")