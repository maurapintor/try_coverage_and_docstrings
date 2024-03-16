"""Main functions."""


def f(a: float) -> float:
    """
    Return the same value.

    Parameters
    ----------
    a : float
        A floating number.

    Returns
    -------
    any
        The same as the input a.
    """
    return a


def g(b: float) -> str:
    """
    Convert to string.

    Parameters
    ----------
    b : number
        Number, either integer or float.

    Returns
    -------
    string
        The input b as a string.
    """
    return str(b)


def func_l(x: float | str) -> bool:
    """
    Check if the input is a string.

    Parameters
    ----------
    x : float | str
        A float or a string

    Returns
    -------
    bool
        True if the input is a string.
    """
    return isinstance(x, str)
