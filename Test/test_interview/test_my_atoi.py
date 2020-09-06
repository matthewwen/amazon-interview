import pytest
from Interview.MyAtoi.MyAtoi import Solution


@pytest.fixture
def _obj_solution():
    return Solution()


def test_simple(_obj_solution):
    response = _obj_solution.myAtoi("42")
    assert response == 42


def test_with_words_is_successful(_obj_solution):
    response = _obj_solution.myAtoi("4193 with words")
    assert response == 4193


def test_with_words_is_unsuccessful(_obj_solution):
    response = _obj_solution.myAtoi("words and 987")
    assert response == 0


def test_negative_is_successful(_obj_solution):
    response = _obj_solution.myAtoi("-9333")
    assert response == -9333


def test_with_long_number_is_unsuccessful(_obj_solution):
    response = _obj_solution.myAtoi("-91283472332")
    assert response == -2147483648


def test_with_corner_long_number_is_unsuccessful(_obj_solution):
    response = _obj_solution.myAtoi("-2147483649")
    assert response == -2147483648


def test_with_0_padding_is_successful(_obj_solution):
    response = _obj_solution.myAtoi("-000000000000001")
    assert response == -1


def test_with_plus_is_successful(_obj_solution):
    response = _obj_solution.myAtoi("+000000000000001")
    assert response == 1


def test_with_plus_is_unsuccessful(_obj_solution):
    response = _obj_solution.myAtoi("00000+0000000001")
    assert response == 0
