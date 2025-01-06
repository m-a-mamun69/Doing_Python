# Generate a URL Safe Token
import secrets

url_token = secrets.token_urlsafe(16)
print("URL Safe Token: ", url_token)