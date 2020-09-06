import pytest

from Interview.MedianOfTwoSortedArrays.main import Solution


@pytest.fixture
def _get_obj():
    return Solution()


def test_example_1(_get_obj):
    response = _get_obj.findMedianSortedArrays([1, 3], [2])
    assert response == 2


def test_example_2(_get_obj):
    response = _get_obj.findMedianSortedArrays([1, 2], [3, 4])
    assert response == 2.5


def test_odd_number_input(_get_obj):
    response = _get_obj.findMedianSortedArrays([1, 2, 4], [3, 5])
    assert response == 3


def test_same_number_is_successful(_get_obj):
    response = _get_obj.findMedianSortedArrays([0, 0], [0, 0])
    assert response == 0


def test_empty_list_is_successful(_get_obj):
    response = _get_obj.findMedianSortedArrays([], [1])
    assert response == 1
    response = _get_obj.findMedianSortedArrays([2], [])
    assert response == 2

