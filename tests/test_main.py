from project.functions.main_functions import f, func_l, g


def test_function_string() -> None:
    assert f(a="a") == "a", "Should be a"


def test_function_number() -> None:
    assert f(a=1) == 1, "Should be 1"


def test_function_g() -> None:
    assert g(b=1) == "1", "Should be 1"


def test_function_l() -> None:
    assert func_l(x="a") is True, "Should be True"
