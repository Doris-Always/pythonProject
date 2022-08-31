import string


def password(strong_passcode: str):
    value_validation = True
    length_of_password = len(strong_passcode)
    character = string.punctuation

    if length_of_password != 6:
        value_validation = False
        # print("perfect")

    if not any(check_case.islower() for check_case in strong_passcode):
        print("you must include a lower case")

        value_validation = False
    if not any(check_case.isupper() for check_case in strong_passcode):
        print("you must have at least one upper case")
        value_validation = False
    if not any(check_digit.isdigit() for check_digit in strong_passcode):
        print("you must have at least a digit in your password")
        value_validation = False
    if not any(check_character in character for check_character in strong_passcode):
        print("you must add a special character")
        value_validation = False
    if value_validation:
        print("password successfully generated")
    else:
        print("re-add your password")


passcode = str(input("Enter your password: "))
password(passcode)
