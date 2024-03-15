

from project.functions.main_functions import f, g, l


def test_function_string():
    assert f("a") == "a", "Should be a"

def test_function_number():
    assert f(1) == 1, "Should be 1"

def test_function_g():
   assert g(1) == "1", "Should be 1"

def test_function_l():
    assert l("a") == True, "Should be True"
