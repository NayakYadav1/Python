class InvalidEmailError(Exception):
    pass

raise InvalidEmailError("The email address provided is not in valid format")