def subStringK(input, k):
    window = set()
    result = set()

    start = 0
    for end, v in enumerate(input):
        if v in window:
            start = start + 1
        else:
            window.add(v)

        if len(window) == k:
            result.add(input[start: end + 1])
            start = start + 1
            window.remove(input[start])

    return list(result)
