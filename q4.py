import re

def validate_number_plate(number_plate):
    pattern = r"^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$"
    
    if re.match(pattern, number_plate):
        return True
    else:
        return False


# Example usage
number_plate = input("Enter the number plate: ")
if validate_number_plate(number_plate):
    print("Valid number plate")
else:
    print("Invalid number plate")