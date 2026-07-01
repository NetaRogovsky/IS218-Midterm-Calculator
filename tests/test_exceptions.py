from app.exceptions import (
    CalculatorError,
    OperationError,
    ValidationError,
    ConfigError,
)


def test_operation_error_is_calculator_error():
    assert issubclass(OperationError, CalculatorError)


def test_validation_error_is_calculator_error():
    assert issubclass(ValidationError, CalculatorError)


def test_config_error_is_calculator_error():
    assert issubclass(ConfigError, CalculatorError)


def test_raise_and_catch():
    try:
        raise OperationError("boom")
    except CalculatorError as e:
        assert str(e) == "boom"