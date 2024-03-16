from project.functions.another_function import p


def test_another_function():
    assert p(3) == float(3), "Should be 3"
