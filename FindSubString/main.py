def get_explanation(input, k):
    window_set = dict()
    result = list()

    start, end = 0, 0
    last = None
    for end, item in enumerate(input):
        if item in window_set:
            window_set[item] = window_set[item] + 1
        else:
            result = result + get_explanation(input[start + 1: end], k)
            while len(window_set) == k:
                window_set[input[start]] = window_set[input[start]] - 1
                if window_set[input[start]] <= 0:
                    window_set.pop(input[start])
                start = start + 1
            window_set[item] = 1

        if len(window_set) == k:
            last = input[start: end + 1]
            result.append(last)

    if last is not None and len(last) > k:
        while len(window_set) == k:
            window_set[input[start]] = window_set[input[start]] - 1
            if window_set[input[start]] == 0:
                window_set.pop(input[start])
            else:
                start = start + 1
                result.append(input[start: end + 1])
    return result
