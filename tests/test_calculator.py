from project.utils.calculator import calc_sum


def test_calc_sum():
    assert calc_sum(1, 3) == 4, "Should be 4"
