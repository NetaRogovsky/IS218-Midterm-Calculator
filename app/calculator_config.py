import os
from dotenv import load_dotenv
from app.exceptions import ConfigError

load_dotenv()


def _get_bool(name, default):
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() == "true"


class CalculatorConfig:
    """Loads and validates configuration from environment variables."""

    def __init__(self):
        self.log_dir = os.getenv("CALCULATOR_LOG_DIR", "logs")
        self.history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "history")
        self.max_history_size = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
        self.auto_save = _get_bool("CALCULATOR_AUTO_SAVE", True)
        self.precision = int(os.getenv("CALCULATOR_PRECISION", "10"))
        self.max_input_value = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000"))
        self.encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
        self.validate()

    @property
    def log_file(self):
        return os.path.join(self.log_dir, "calculator.log")

    @property
    def history_file(self):
        return os.path.join(self.history_dir, "history.csv")

    def validate(self):
        # LBYL: check values before the app uses them
        if self.max_history_size <= 0:
            raise ConfigError("Max history size must be positive.")
        if self.precision < 0:
            raise ConfigError("Precision cannot be negative.")
        if self.max_input_value <= 0:
            raise ConfigError("Max input value must be positive.")