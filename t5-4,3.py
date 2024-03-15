import re

def validate_usa_telephone_number(number):
    
    #Validates if a given string matches the USA telephone number format (###-###-####).

    #Args:
    #number (str): The telephone number to validate.

    #Returns:
    #bool: True if the number matches the format, False otherwise.
    
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(pattern.match(number))
def main():
    number = input("Enter a telephone number in the format ###-###-####: ")
    if validate_usa_telephone_number(number):
        print("Valid USA telephone number.")
    else:
        print("Invalid USA telephone number.")

if __name__ == "__main__":
    main()
