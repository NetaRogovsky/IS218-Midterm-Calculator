class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class OperationError(CalculatorError):
    """Raised when an operation fails (e.g. division by zero)."""
    pass


class ValidationError(CalculatorError):
    """Raised when user input fails validation."""
    pass


class ConfigError(CalculatorError):
    """Raised when configuration is invalid."""
    pass