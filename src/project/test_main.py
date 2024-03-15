from functions.main_functions import f


def test_function_string():
    assert f("a") == "a", "Should be a"

def test_function_number():
    assert f(1) == 1, "Should be 1"

