from app.exceptions import OperationError


class Operation:
    """Base strategy for an operation."""

    def execute(self, a, b):
        raise NotImplementedError  # pragma: no cover


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Subtraction(Operation):
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot take the 0th root.")
        if a < 0:
            raise OperationError("Cannot take the root of a negative number.")
        return a ** (1 / b)


class Modulus(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot take modulus by zero.")
        return a % b


class IntegerDivision(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a // b


class Percentage(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot calculate percentage with zero total.")
        return (a / b) * 100


class AbsoluteDifference(Operation):
    def execute(self, a, b):
        return abs(a - b)


class OperationFactory:
    """Factory pattern: creates operation strategy objects."""

    _operations = {
        "add": Addition,
        "subtract": Subtraction,
        "multiply": Multiplication,
        "divide": Division,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntegerDivision,
        "percent": Percentage,
        "abs_diff": AbsoluteDifference,
    }

    @classmethod
    def create(cls, name):
        operation_class = cls._operations.get(name)
        if operation_class is None:
            raise OperationError(f"Unknown operation: {name}")
        return operation_class()