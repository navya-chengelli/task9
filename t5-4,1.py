import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    email = input("Enter an email address to validate: ")
    if validate_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")

if __name__ == "__main__":
    main()

