import os
import logging


class Logger:
    """Wraps Python's logging module to log calculator events to a file."""

    def __init__(self, config):
        self.config = config
        os.makedirs(config.log_dir, exist_ok=True)
        self.logger = logging.getLogger("calculator")
        self.logger.setLevel(logging.INFO)
        # clear old handlers so each Logger writes to its own configured file
        for old_handler in list(self.logger.handlers):
            self.logger.removeHandler(old_handler)
            old_handler.close()
        handler = logging.FileHandler(config.log_file, encoding=config.encoding)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)