import os
import pandas as pd
from app.calculation import Calculation
from app.exceptions import OperationError


class HistoryObserver:
    """Base observer."""

    def update(self, calculation):
        raise NotImplementedError  # pragma: no cover


class LoggingObserver(HistoryObserver):
    """Observer that logs each calculation to the log file."""

    def __init__(self, logger):
        self.logger = logger

    def update(self, calculation):
        self.logger.info(
            f"Calculation: {calculation.operation} "
            f"({calculation.a}, {calculation.b}) = {calculation.result}"
        )


class AutoSaveObserver(HistoryObserver):
    """Observer that auto-saves history to CSV whenever a calculation happens."""

    def __init__(self, history_manager):
        self.history_manager = history_manager

    def update(self, calculation):
        if self.history_manager.config.auto_save:
            self.history_manager.save()


class HistoryManager:
    """Manages calculation history with a pandas DataFrame and observers."""

    COLUMNS = ["operation", "a", "b", "result", "timestamp"]

    def __init__(self, config):
        self.config = config
        self.calculations = []
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, calculation):
        for observer in self._observers:
            observer.update(calculation)

    def add_calculation(self, calculation):
        self.calculations.append(calculation)
        if len(self.calculations) > self.config.max_history_size:
            self.calculations.pop(0)
        self.notify(calculation)

    def get_dataframe(self):
        if not self.calculations:
            return pd.DataFrame(columns=self.COLUMNS)
        return pd.DataFrame([c.to_dict() for c in self.calculations])

    def is_empty(self):
        return len(self.calculations) == 0

    def clear(self):
        self.calculations = []

    def set_state(self, calculations):
        self.calculations = list(calculations)

    def get_state(self):
        return list(self.calculations)

    def save(self):
        os.makedirs(self.config.history_dir, exist_ok=True)
        df = self.get_dataframe()
        df.to_csv(self.config.history_file, index=False, encoding=self.config.encoding)

    def load(self):
        if not os.path.exists(self.config.history_file):
            raise OperationError("No history file found to load.")
        try:
            df = pd.read_csv(self.config.history_file, encoding=self.config.encoding)
        except pd.errors.EmptyDataError:
            self.calculations = []
            return
        self.calculations = [Calculation.from_dict(row) for row in df.to_dict("records")]