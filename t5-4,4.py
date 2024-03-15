import re

def validate_password(password):
    # 16 characters
    # Contains at least one uppercase letter
    # Contains at least one lowercase letter
    # Contains at least one digit
    # Contains at least one special character from !@#$%^&*()-_+=
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=])[A-Za-z\d!@#$%^&*()-_+=]{16}$'
    if re.match(pattern, password):
        return True
    else:
        return False

def main():
    password = input("Enter a 16-character password to validate: ")
    if validate_password(password):
        print("Valid password")
    else:
        print("Invalid password")

if __name__ == "__main__":
    main()



