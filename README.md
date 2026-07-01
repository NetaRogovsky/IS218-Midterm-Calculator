# IS218 Midterm - Advanced Command-Line Calculator

An advanced command-line calculator built in Python that integrates multiple design patterns, pandas-based history management, logging, configuration via environment variables, and full test automation with GitHub Actions.

## Features
- REPL interface with colored output (colorama)
- Operations: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
- Commands: history, clear, undo, redo, save, load, help, exit
- Calculation history stored in a pandas DataFrame and saved to CSV with timestamps
- Automatic saving and logging on every calculation
- Configuration loaded from environment variables via a .env file
- Comprehensive error handling using both LBYL and EAFP styles
- 90%+ test coverage enforced in CI

## Design patterns
- Factory: creates operation objects based on user input
- Strategy: each operation is an interchangeable execution strategy
- Observer: LoggingObserver and AutoSaveObserver react to new calculations
- Memento: undo/redo by saving and restoring history state
- Facade: the Calculator class provides a simple interface over all subsystems

## Project structure