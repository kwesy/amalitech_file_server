from django.core.exceptions import ValidationError
import re

def validate_password_special_and_capital(value):

    special_pattern = r'[!@#$%^&*(),.?":{}|<>]'
    capital_pattern = r'[A-Z]'

    # Check if the password contains at least one special symbol
    if not re.search(special_pattern, value):
        raise ValidationError("Password must contain at least one special symbol.")

    # Check if the password contains at least one capital letter
    if not re.search(capital_pattern, value):
        raise ValidationError("Password must contain at least one capital letter.")
