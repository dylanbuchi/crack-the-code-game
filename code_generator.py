import random


class CodeGenerator:
    """Class to generate a secret code of integers"""
    def __init__(self, total_digits: int = 4):
        self.total_digits = total_digits

    def create_digits_code_list(self):
        digits = []
        for _ in range(self.total_digits):
            digits.append(random.randint(0, 9))
        return digits