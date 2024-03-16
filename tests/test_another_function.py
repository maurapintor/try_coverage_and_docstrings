from project.functions.another_function import another, p


def test_p_function() -> None:
    assert p(3) == float(3), "Should be 3"


def test_another_function() -> None:
    assert another(3) == "False", "Should be False"
