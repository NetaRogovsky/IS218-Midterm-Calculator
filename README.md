# IS218 Midterm - Advanced Command-Line Calculator

An advanced command-line calculator built in Python using multiple design patterns, pandas-based history management, logging, environment-based configuration, and automated testing with GitHub Actions.

## Features
- REPL interface with colored output (colorama)
- Operations: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
- Commands: history, clear, undo, redo, save, load, help, exit
- History stored in a pandas DataFrame and saved to CSV with timestamps
- Auto-saving and logging on every calculation
- Configuration loaded from a .env file
- Error handling using both LBYL and EAFP styles
- 90%+ test coverage enforced in CI

## Design patterns
- Factory: creates operation objects from user input
- Strategy: each operation is an interchangeable class
- Observer: LoggingObserver and AutoSaveObserver react to new calculations
- Memento: powers undo and redo
- Facade: the Calculator class hides all subsystems behind a simple interface

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Create a `.env` file in the project root:
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8

## Run
```bash
python3 main.py
```

## Test
```bash
pytest
```

## CI/CD
GitHub Actions runs all tests on every push and pull request to main and fails the build if coverage drops below 90%.