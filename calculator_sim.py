class Calculator:
    def __init__(self):
        self.last_result = 0

    def add(self, number1, number2):
        self.last_result = number1 + number2
        return number1 + number2

    def subtract(self, number1, number2):
        self.last_result = number1 - number2
        return number1 - number2

    def multiply(self, number1, number2):
        self.last_result = number1 * number2
        return number1 * number2

    def divide(self, number1, number2):
        self.last_result = number1 / number2
        return number1 / number2
