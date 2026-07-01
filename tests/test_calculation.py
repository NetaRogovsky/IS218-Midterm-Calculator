import pytest
from app.calculation import Calculation


@pytest.mark.parametrize("operation, a, b, expected", [
    ("add", 2, 3, 5),
    ("modulus", 10, 3, 1),
    ("abs_diff", 3, 8, 5),
])
def test_calculation_result(operation, a, b, expected):
    assert Calculation(operation, a, b).result == expected


def test_calculation_str():
    assert str(Calculation("add", 2, 3)) == "2 + 3 = 5"


def test_calculation_has_timestamp():
    calc = Calculation("add", 2, 3)
    assert calc.timestamp is not None


def test_to_dict():
    d = Calculation("add", 2, 3).to_dict()
    assert d["operation"] == "add"
    assert d["result"] == 5
    assert "timestamp" in d


def test_from_dict():
    data = {"operation": "add", "a": 2, "b": 3, "result": 5, "timestamp": "2024-01-01"}
    calc = Calculation.from_dict(data)
    assert calc.result == 5
    assert calc.timestamp == "2024-01-01"