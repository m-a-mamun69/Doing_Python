# Generate a Secure Random Token

import secrets

token = secrets.token_hex(16)
print("Secure Token: ", token)