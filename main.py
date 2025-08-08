from typing_extensions import Union


class Calculator:
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b


if __name__ == "__main__":
    calculator = Calculator()
