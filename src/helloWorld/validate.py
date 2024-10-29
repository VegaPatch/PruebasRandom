import re

def validate(name):
    valid_characters = r'^[a-zA-Z]+$'
    if re.match(valid_characters, name):
        return True
    else:
        return False
