import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigError


def test_config_defaults():
    config = CalculatorConfig()
    assert config.max_history_size > 0
    assert config.precision >= 0
    assert config.encoding


def test_config_paths():
    config = CalculatorConfig()
    assert config.log_file.endswith("calculator.log")
    assert config.history_file.endswith("history.csv")


def test_config_custom(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "50")
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    monkeypatch.setenv("CALCULATOR_PRECISION", "2")
    config = CalculatorConfig()
    assert config.max_history_size == 50
    assert config.auto_save is False
    assert config.precision == 2


def test_config_auto_save_true(monkeypatch):
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "true")
    assert CalculatorConfig().auto_save is True


def test_config_invalid_history(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "0")
    with pytest.raises(ConfigError):
        CalculatorConfig()


def test_config_invalid_precision(monkeypatch):
    monkeypatch.setenv("CALCULATOR_PRECISION", "-1")
    with pytest.raises(ConfigError):
        CalculatorConfig()


def test_config_invalid_max_input(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "0")
    with pytest.raises(ConfigError):
        CalculatorConfig()