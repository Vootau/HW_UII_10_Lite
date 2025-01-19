class NegativeNumberError(Exception):
    def __init__(self, number, message="Нельзя использовать отрицательные числа"):
        super().__init__(message)
        self.number = number
        self.message = message

    def __str__(self):
        return f"{self.message}: {self.number}"


def check_positive_number(number):
    if number <= 0:
        raise NegativeNumberError(number)
    else:
        print(f"{number} положительное число.")


# Проверка на неотрицательность
try:
    check_positive_number(-10)
except NegativeNumberError as e:
    print(e)

# корректный ввод
try:
    check_positive_number(20)
except NegativeNumberError as e:
    print(e)
