from colorama import Fore, Style, init
from app.calculator import Calculator
from app.exceptions import CalculatorError

init(autoreset=True)


def build_help(operations):
    lines = ["\nAvailable commands:"]
    lines.append("  Operations: " + ", ".join(operations))
    lines.append("  history - show calculation history")
    lines.append("  clear   - clear the history")
    lines.append("  undo    - undo the last change")
    lines.append("  redo    - redo the last undone change")
    lines.append("  save    - save history to CSV")
    lines.append("  load    - load history from CSV")
    lines.append("  help    - show this message")
    lines.append("  exit    - quit the calculator")
    return "\n".join(lines)


def calculator_repl(calculator=None):
    calc = calculator or Calculator()
    print(Fore.CYAN + "Welcome to the Advanced Python Calculator!")
    print("Type 'help' for commands or 'exit' to quit.")

    while True:
        command = input(Fore.YELLOW + "\n>>> " + Style.RESET_ALL).strip().lower()

        if command == "exit":
            print(Fore.CYAN + "Goodbye!")
            break

        if command == "help":
            print(build_help(calc.operations))
            continue

        if command == "history":
            if calc.history.is_empty():
                print("No calculations yet.")
            else:
                print(calc.history.get_dataframe().to_string(index=False))
            continue

        if command == "clear":
            calc.clear()
            print(Fore.GREEN + "History cleared.")
            continue

        if command == "undo":
            print(Fore.GREEN + "Undo successful." if calc.undo()
                  else Fore.RED + "Nothing to undo.")
            continue

        if command == "redo":
            print(Fore.GREEN + "Redo successful." if calc.redo()
                  else Fore.RED + "Nothing to redo.")
            continue

        if command == "save":
            calc.save()
            print(Fore.GREEN + "History saved.")
            continue

        if command == "load":
            try:
                calc.load()
                print(Fore.GREEN + "History loaded.")
            except CalculatorError as e:
                print(Fore.RED + f"Error: {e}")
            continue

        if command not in calc.operations:
            print(Fore.RED + f"Unknown command '{command}'. Type 'help' for options.")
            continue

        # EAFP: attempt the calculation, handle any calculator error
        try:
            a = input("Enter first number: ").strip()
            b = input("Enter second number: ").strip()
            result = calc.calculate(command, a, b)
            print(Fore.GREEN + f"Result: {result}")
        except CalculatorError as e:
            print(Fore.RED + f"Error: {e}")