import pytest
from app.operations import (
    OperationFactory,
    Division,
    Root,
    Modulus,
    IntegerDivision,
    Percentage,
    AbsoluteDifference,
)
from app.exceptions import OperationError


@pytest.mark.parametrize("name, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 2, 3),
    ("multiply", 4, 3, 12),
    ("divide", 10, 2, 5.0),
    ("power", 2, 3, 8),
    ("root", 9, 2, 3.0),
    ("modulus", 10, 3, 1),
    ("int_divide", 7, 2, 3),
    ("percent", 50, 200, 25.0),
    ("abs_diff", 3, 8, 5),
])
def test_factory_operations(name, a, b, expected):
    op = OperationFactory.create(name)
    assert op.execute(a, b) == expected


def test_factory_unknown():
    with pytest.raises(OperationError, match="Unknown operation"):
        OperationFactory.create("banana")


def test_division_by_zero():
    with pytest.raises(OperationError, match="divide by zero"):
        Division().execute(5, 0)


def test_root_zero():
    with pytest.raises(OperationError, match="0th root"):
        Root().execute(9, 0)


def test_root_negative():
    with pytest.raises(OperationError, match="negative"):
        Root().execute(-9, 2)


def test_modulus_zero():
    with pytest.raises(OperationError, match="modulus by zero"):
        Modulus().execute(5, 0)


def test_int_divide_zero():
    with pytest.raises(OperationError, match="divide by zero"):
        IntegerDivision().execute(5, 0)


def test_percent_zero():
    with pytest.raises(OperationError, match="zero total"):
        Percentage().execute(5, 0)


def test_abs_diff():
    assert AbsoluteDifference().execute(10, 3) == 7