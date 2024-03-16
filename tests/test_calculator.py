from project.utils.calculator import calc_sum

RES: int = 4


def test_calc_sum() -> None:
    assert calc_sum(a=1, b=3) == RES, "Should be 4"
