from app.exceptions import ValidationError


def validate_number(value, max_value=None):
    """EAFP: try to convert, raise a clear error if it fails."""
    try:
        number = float(value)
    except (ValueError, TypeError):
        raise ValidationError(f"'{value}' is not a valid number.")
    # LBYL: check range after conversion
    if max_value is not None and abs(number) > max_value:
        raise ValidationError(f"Value {number} exceeds the maximum of {max_value}.")
    return number


def validate_operation(name, valid_operations):
    """LBYL: check membership before returning."""
    if name not in valid_operations:
        raise ValidationError(f"'{name}' is not a valid operation.")
    return name