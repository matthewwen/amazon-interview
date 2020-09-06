import pytest
from Interview.LongestSubString.LengthOfLongestSubString import Solution


@pytest.fixture
def _obj_solution():
    return Solution()


def test_is_successful(_obj_solution):
    response = _obj_solution.lengthOfLongestSubstring("abcabcbb")
    assert response == 3


def test_space_is_successful(_obj_solution):
    response = _obj_solution.lengthOfLongestSubstring(" ")
    assert response == 1
