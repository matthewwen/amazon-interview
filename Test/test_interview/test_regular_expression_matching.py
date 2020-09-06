import pytest

from Interview.RegularExpressionMatching.main import Solution


@pytest.fixture
def _obj():
    return Solution()


def test_is_successful(_obj):
    response = _obj.isMatch("aa", "a")
    assert response == False


def test_star_is_successful(_obj):
    response = _obj.isMatch("aa", "a*")
    assert response == True


def test_dot_is_successful(_obj):
    response = _obj.isMatch("ab", ".*")
    assert response == True


def test_other_is_successful(_obj):
    response = _obj.isMatch("aab", "c*a*b")
    assert response == True
    response = _obj.isMatch("mississippi", "mis*is*p*.")
    assert response == False
    response = _obj.isMatch("aaa", "a*a")
    assert response == True


def test_other_dot_c_is_successful(_obj):
    response = _obj.isMatch("ab", ".*c")
    assert response == False


def test_operation_after_fact(_obj):
    response = _obj.isMatch("aaa", "ab*a*c*a")
    assert response == True


def test_operation_after_fact_simple(_obj):
    response = _obj.isMatch("a", "ab*")
    assert response == True


def test_dot_make_it_equal_is_successful(_obj):
    response = _obj.isMatch("bbbba", ".*a*a")
    assert response == True


def test_make_through_all(_obj):
    response = _obj.isMatch("a", ".*")
    assert response == True
    response = _obj.isMatch("a", ".*.")
    assert response == True


def test_repeat_too_much(_obj):
    response = _obj.isMatch("aaa", "aaaa")
    assert response == False

def test_not_execeed_time(_obj):
    response = _obj.isMatch("a", "..*")
    assert response == True

def test_really_hard(_obj):
    response = _obj.isMatch("b", "a.*")
    assert response == False
