import pytest
from unittest.mock import patch
from app.calculator import Calculator
from app.calculator_repl import calculator_repl, build_help
from app.calculator_config import CalculatorConfig


@pytest.fixture
def config(tmp_path):
    cfg = CalculatorConfig()
    cfg.log_dir = str(tmp_path / "logs")
    cfg.history_dir = str(tmp_path / "history")
    return cfg


def test_calculate(config):
    calc = Calculator(config)
    assert calc.calculate("add", "2", "3").result == 5


def test_undo_redo(config):
    calc = Calculator(config)
    calc.calculate("add", "2", "3")
    assert calc.undo() is True
    assert calc.history.is_empty()
    assert calc.redo() is True
    assert not calc.history.is_empty()


def test_undo_nothing(config):
    assert Calculator(config).undo() is False


def test_redo_nothing(config):
    assert Calculator(config).redo() is False


def test_clear(config):
    calc = Calculator(config)
    calc.calculate("add", "2", "3")
    calc.clear()
    assert calc.history.is_empty()


def test_save_and_load(config):
    calc = Calculator(config)
    calc.calculate("add", "2", "3")
    calc.save()
    calc2 = Calculator(config)
    calc2.load()
    assert not calc2.history.is_empty()


def run_repl(inputs, config):
    with patch("builtins.input", side_effect=inputs):
        with patch("builtins.print"):
            calculator_repl(Calculator(config))


def test_build_help():
    text = build_help(["add", "subtract"])
    assert "add" in text
    assert "exit" in text


def test_repl_exit(config):
    run_repl(["exit"], config)


def test_repl_help(config):
    run_repl(["help", "exit"], config)


def test_repl_history_empty(config):
    run_repl(["history", "exit"], config)


def test_repl_calculation_and_history(config):
    run_repl(["add", "2", "3", "history", "exit"], config)


def test_repl_clear(config):
    run_repl(["add", "2", "3", "clear", "exit"], config)


def test_repl_undo_redo(config):
    run_repl(["add", "2", "3", "undo", "redo", "exit"], config)


def test_repl_undo_nothing(config):
    run_repl(["undo", "exit"], config)


def test_repl_redo_nothing(config):
    run_repl(["redo", "exit"], config)


def test_repl_save(config):
    run_repl(["add", "2", "3", "save", "exit"], config)


def test_repl_load(config):
    calc = Calculator(config)
    calc.calculate("add", "2", "3")
    calc.save()
    with patch("builtins.input", side_effect=["load", "exit"]):
        with patch("builtins.print"):
            calculator_repl(Calculator(config))


def test_repl_load_missing(config):
    run_repl(["load", "exit"], config)


def test_repl_unknown_command(config):
    run_repl(["banana", "exit"], config)


def test_repl_divide_by_zero(config):
    run_repl(["divide", "5", "0", "exit"], config)


def test_repl_invalid_number(config):
    run_repl(["add", "abc", "3", "exit"], config)


def test_repl_all_operations(config):
    run_repl(["modulus", "10", "3", "int_divide", "7", "2",
              "percent", "50", "200", "abs_diff", "3", "8", "exit"], config)