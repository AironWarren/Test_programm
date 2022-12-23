from utils import division
import pytest


# декоратор pytest.mark.parametrize(строка с переменными, лист с кортежами, которые мы распаковываем в переменные)
@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (15, 5, 3)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('a, divider,c', [(ZeroDivisionError, 0, 16),
                                          (TypeError, '2', 25)])
def test_exceptions(a, divider, c):
    with pytest.raises(a):
        division(c, divider)
