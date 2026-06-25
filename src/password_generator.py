import secrets
import string

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(chars) for _ in range(length))
    print(f"\nGenerated Password:\n{password}")
