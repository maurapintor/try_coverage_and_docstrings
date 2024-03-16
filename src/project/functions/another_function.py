"""Returns float numbers."""


def p(x: int) -> float:
    """Return the input as a float.

    Parameters
    ----------
    x : int
        an integer

    Returns
    -------
    float
        the input as float
    """
    return float(x)


def another(x: bool):
    """
    Print a string.

    Parameters
    ----------
    x : bool
        An input.

    Returns
    -------
    str
        True if x is True.
    """
    return "True" if x is True else "False"
