from project.functions.another_function import p, another


def test_p_function():
    assert p(3) == float(3), "Should be 3"


def test_another_function():
    assert another(3) == "False", "Should be False"
