import os
import pytest
from app.history import HistoryManager, LoggingObserver, AutoSaveObserver
from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.logger import Logger
from app.exceptions import OperationError


@pytest.fixture
def config(tmp_path):
    cfg = CalculatorConfig()
    cfg.log_dir = str(tmp_path / "logs")
    cfg.history_dir = str(tmp_path / "history")
    return cfg


@pytest.fixture
def manager(config):
    return HistoryManager(config)


def test_add_calculation(manager):
    manager.add_calculation(Calculation("add", 2, 3))
    assert not manager.is_empty()


def test_logging_observer(manager, config):
    logger = Logger(config)
    manager.add_observer(LoggingObserver(logger))
    manager.add_calculation(Calculation("add", 2, 3))
    with open(config.log_file, encoding="utf-8") as f:
        assert "Calculation" in f.read()


def test_autosave_observer(manager):
    manager.add_observer(AutoSaveObserver(manager))
    manager.add_calculation(Calculation("add", 2, 3))
    assert os.path.exists(manager.config.history_file)


def test_autosave_disabled(manager):
    manager.config.auto_save = False
    manager.add_observer(AutoSaveObserver(manager))
    manager.add_calculation(Calculation("add", 2, 3))
    assert not os.path.exists(manager.config.history_file)


def test_max_history_size(manager):
    manager.config.max_history_size = 2
    for i in range(4):
        manager.add_calculation(Calculation("add", i, 1))
    assert len(manager.get_state()) == 2


def test_clear(manager):
    manager.add_calculation(Calculation("add", 2, 3))
    manager.clear()
    assert manager.is_empty()


def test_save_and_load(manager):
    manager.add_calculation(Calculation("add", 2, 3))
    manager.save()
    new_manager = HistoryManager(manager.config)
    new_manager.load()
    assert not new_manager.is_empty()


def test_load_missing_file(manager):
    with pytest.raises(OperationError, match="No history file"):
        manager.load()


def test_load_empty_file(manager):
    os.makedirs(manager.config.history_dir, exist_ok=True)
    open(manager.config.history_file, "w").close()
    manager.load()
    assert manager.is_empty()


def test_get_dataframe_empty(manager):
    df = manager.get_dataframe()
    assert df.empty


def test_get_and_set_state(manager):
    manager.add_calculation(Calculation("add", 2, 3))
    state = manager.get_state()
    manager.clear()
    manager.set_state(state)
    assert not manager.is_empty()