def divide(x, y):
    """
    Args:
        x: The Dividend.
        y: The Divisor.
    
    Returns:
        The Quotient.
    """
    if y == 0:
        raise ValueError("Division by zero")
    return x / y