import pytest
from app.input_validators import validate_number, validate_operation
from app.exceptions import ValidationError


@pytest.mark.parametrize("value, expected", [
    ("5", 5.0),
    ("3.14", 3.14),
    ("-2", -2.0),
])
def test_validate_number_valid(value, expected):
    assert validate_number(value) == expected


@pytest.mark.parametrize("value", ["abc", "", None])
def test_validate_number_invalid(value):
    with pytest.raises(ValidationError):
        validate_number(value)


def test_validate_number_exceeds_max():
    with pytest.raises(ValidationError, match="exceeds the maximum"):
        validate_number("5000", max_value=1000)


def test_validate_number_within_max():
    assert validate_number("500", max_value=1000) == 500.0


def test_validate_operation_valid():
    assert validate_operation("add", ["add", "subtract"]) == "add"


def test_validate_operation_invalid():
    with pytest.raises(ValidationError):
        validate_operation("banana", ["add", "subtract"])