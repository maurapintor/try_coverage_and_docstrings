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


def another(x: str) -> bool:
    """
    Print a string.

    Parameters
    ----------
    x : str
        An input.

    Returns
    -------
    bool
        True if x is not empty
    """
    return x != ""
