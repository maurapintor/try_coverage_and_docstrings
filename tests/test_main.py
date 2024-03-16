from project.functions.main_functions import f, g, func_l


def test_function_string():
    assert f("a") == "a", "Should be a"


def test_function_number():
    assert f(1) == 1, "Should be 1"


def test_function_g():
    assert g(1) == "1", "Should be 1"


def test_function_l():
    assert func_l("a") is True, "Should be True"
