import pytest

from Interview.FindSubStringIdx.findsubstring import Solution


@pytest.fixture
def _obj():
    return Solution()


def test_is_successful(_obj):
    response = _obj.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print(response)
