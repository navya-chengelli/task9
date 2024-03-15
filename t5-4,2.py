import re

def validate_bangladesh_mobile_number(number):
    
    #Validates if a given string matches the Bangladesh mobile number format (01#########).

    #Args:
    #number (str): The mobile number to validate.

    #Returns:
    #bool: True if the number matches the format, False otherwise.
    
    pattern = re.compile(r'^01\d{9}$')
    return bool(pattern.match(number))
def main():
    number = input("Enter a mobile number in the format 01#########: ")
    if validate_bangladesh_mobile_number(number):
        print("Valid Bangladesh mobile number.")
    else:
        print("Invalid Bangladesh mobile number.")

if __name__ == "__main__":
    main()