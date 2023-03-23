import re


class Validatior:
    @staticmethod
    def isValidEmail(email):
        pattern = "^\w+[_.-]?\w+[@]+[a-z]+[.]\w{2,3}$"
        if re.search(pattern, email):
            return True
        return False

    @staticmethod
    def isValidName(name):
        if len(name) > 30:
            return False
        elif re.fullmatch("[A-Za-z ]+", name):
            return True
        return False

    @staticmethod
    def isValidSurname(surname):
        if len(surname) > 30:
            return False
        elif re.fullmatch("[A-Za-z ]+", surname) or surname == '':
            return True
        return False

    @staticmethod
    def isValidGender(gender):
        if gender.strip() in ('male', 'female', ''):
            return True
        return False

    @staticmethod
    def isValidPhone(number):
        digits = number[4:]
        if number.startswith("+374") and len(number) == 12 \
                and digits.isdigit() and digits[0] in '9743':
            return True
        return False
