from Interview.MostCommonWord.main import Solution
import pytest


@pytest.fixture
def _obj_solution():
    return Solution()


def test_is_successful(_obj_solution):
    response = _obj_solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    assert response == "ball"


def test_commas_is_successful(_obj_solution):
    response = _obj_solution.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])
    assert response == "b"
