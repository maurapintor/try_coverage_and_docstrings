from project.functions.another_function import another, p


def test_p_function() -> None:
    assert p(x=3) == float(3), "Should be 3"


def test_another_function() -> None:
    assert another(x="a") is True, "Should be False"
