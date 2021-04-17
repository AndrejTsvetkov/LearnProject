import re


def is_correct_password(string):
    if bool(re.search(r'(?=.*[0-9])(?=.*[!@#$%^№\-&*?.,()\[\]"\'+:;>=>/_{}|` ])(?=.*[a-z])(?=.*[A-Z])', string)) and 6 <= len(string) <= 12:
        return True
    else:
        return False


string = "Psпалпо1&"
print(is_correct_password(string))