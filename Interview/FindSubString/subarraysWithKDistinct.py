class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window_set = dict()
        result = 0

        start, end = 0, 0
        last = None
        for end, item in enumerate(A):
            if item in window_set:
                window_set[item] = window_set[item] + 1
            else:
                result = result + self.subarraysWithKDistinct(A[start + 1: end], K)
                while len(window_set) == K:
                    window_set[A[start]] = window_set[A[start]] - 1
                    if window_set[A[start]] <= 0:
                        window_set.pop(A[start])
                    start = start + 1
                window_set[item] = 1

            if len(window_set) == K:
                last = A[start: end + 1]
                result += 1

        if last is not None and len(last) > K:
            while len(window_set) == K:
                window_set[A[start]] = window_set[A[start]] - 1
                if window_set[A[start]] == 0:
                    window_set.pop(A[start])
                else:
                    start += 1
                    result += 1
        return result

