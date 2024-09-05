# test sum

import pytest

from src.ej1 import my_sum


def test_my_sum():
    assert my_sum(1, 2) == 3
    assert my_sum(0, 0) == 0
    assert my_sum(-1, 1) == 0
    assert my_sum(-1, -1) == -2
    assert my_sum(1, -1) == 0
