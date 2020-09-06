from Interview.PairGivenSum.PairGivenSum import findPair


def test1():
    response = findPair([1, 10, 25, 35, 60], 90)
    response.sort()
    assert [2, 3] == response


def test2():
    response = findPair([20, 50, 40, 25, 30, 10], 90)
    response.sort()
    assert [1, 5] == response
