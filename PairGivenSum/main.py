def findPair(nums, target):
    [idx1, idx2] = [-1, -1]

    map = dict()
    for i, v in enumerate(nums):
        otherPair = target - 30 - v
        if otherPair in map:
            if [idx1, idx2] == [-1, -1] or max([nums[idx1], nums[idx2]]) < max([v, otherPair]):
                [idx1, idx2] = [i, map[otherPair]]
        map[v] = i

    return [idx1, idx2]
