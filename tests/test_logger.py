import os
from app.logger import Logger
from app.calculator_config import CalculatorConfig


def make_config(tmp_path):
    config = CalculatorConfig()
    config.log_dir = str(tmp_path / "logs")
    return config


def test_logger_creates_file(tmp_path):
    logger = Logger(make_config(tmp_path))
    logger.info("test message")
    assert os.path.exists(logger.config.log_file)


def test_logger_levels(tmp_path):
    logger = Logger(make_config(tmp_path))
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    with open(logger.config.log_file, encoding="utf-8") as f:
        content = f.read()
    assert "info" in content
    assert "warning" in content
    assert "error" in content