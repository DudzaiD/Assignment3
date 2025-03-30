def classify_number(n):
    """
    Classifies a number as Positive, Negative, or Zero.

    Parameters:
    n (int): The integer to classify.

    Returns:
    str: "Positive" if n > 0, "Negative" if n < 0, or "Zero" if n == 0.
    """
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
