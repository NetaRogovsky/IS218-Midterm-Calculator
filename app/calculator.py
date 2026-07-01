from app.calculator_config import CalculatorConfig
from app.calculation import Calculation
from app.operations import OperationFactory
from app.history import HistoryManager, LoggingObserver, AutoSaveObserver
from app.calculator_memento import Caretaker
from app.input_validators import validate_number, validate_operation
from app.logger import Logger


class Calculator:
    """Facade: provides a simple interface over config, history, logging, and undo/redo."""

    def __init__(self, config=None):
        self.config = config or CalculatorConfig()
        self.logger = Logger(self.config)
        self.history = HistoryManager(self.config)
        self.history.add_observer(LoggingObserver(self.logger))
        self.history.add_observer(AutoSaveObserver(self.history))
        self.caretaker = Caretaker()
        self.operations = list(OperationFactory._operations.keys())

    def calculate(self, operation, a, b):
        validate_operation(operation, self.operations)
        a = validate_number(a, self.config.max_input_value)
        b = validate_number(b, self.config.max_input_value)
        self.caretaker.save(self.history.get_state())
        calculation = Calculation(operation, a, b)
        self.history.add_calculation(calculation)
        self.logger.info(f"Performed {operation} on {a} and {b}")
        return calculation

    def undo(self):
        state = self.caretaker.undo(self.history.get_state())
        if state is None:
            return False
        self.history.set_state(state)
        return True

    def redo(self):
        state = self.caretaker.redo(self.history.get_state())
        if state is None:
            return False
        self.history.set_state(state)
        return True

    def clear(self):
        self.caretaker.save(self.history.get_state())
        self.history.clear()

    def save(self):
        self.history.save()

    def load(self):
        self.history.load()