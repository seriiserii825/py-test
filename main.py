from typing_extensions import Union


class Calculator:
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be int or float")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be int or float")
        return a * b


if __name__ == "__main__":
    calculator = Calculator()
