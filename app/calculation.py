from datetime import datetime
from app.operations import OperationFactory


class Calculation:
    """Represents a single calculation using a strategy from the factory."""

    SYMBOLS = {
        "add": "+",
        "subtract": "-",
        "multiply": "*",
        "divide": "/",
        "power": "^",
        "root": "root",
        "modulus": "%",
        "int_divide": "//",
        "percent": "% of",
        "abs_diff": "|diff|",
    }

    def __init__(self, operation, a, b, result=None, timestamp=None):
        self.operation = operation
        self.a = a
        self.b = b
        if result is None:
            self.result = OperationFactory.create(operation).execute(a, b)
        else:
            self.result = result
        self.timestamp = timestamp or datetime.now().isoformat()

    def __str__(self):
        symbol = self.SYMBOLS[self.operation]
        return f"{self.a} {symbol} {self.b} = {self.result}"

    def to_dict(self):
        return {
            "operation": self.operation,
            "a": self.a,
            "b": self.b,
            "result": self.result,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["operation"],
            data["a"],
            data["b"],
            result=data["result"],
            timestamp=data.get("timestamp"),
        )