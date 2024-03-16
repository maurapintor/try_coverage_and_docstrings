"""Main functions."""


def f(a):
    """
    Return the same value.

    Parameters
    ----------
    a : any
        Anything.

    Returns
    -------
    any
        The same as the input a.
    """
    return a


def g(b):
    """
    Convert to string.

    Parameters
    ----------
    b : any
        Any input that will be returned as string.

    Returns
    -------
    any
        The input b as a string.
    """
    return str(b)


def func_l(x, a):
    """
    Check if the input is a string.

    Parameters
    ----------
    x : any
        Any object.
    y: any
        BS argument.

    Returns
    -------
    bool
        True if the input is a string.
    """
    return isinstance(x, str)
