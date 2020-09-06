from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)

        left, right, prev_median, median = 0, 0, 0, 0
        for i in range(int(length / 2) + 1):
            if left >= len(nums1):
                prev_median = median
                median = nums2[right]
                right += 1
            elif right >= len(nums2):
                prev_median = median
                median = nums1[left]
                left += 1
            elif nums1[left] < nums2[right]:
                prev_median = median
                median = nums1[left]
                left += 1
            else:
                prev_median = median
                median = nums2[right]
                right += 1

        if length % 2 == 0:
            return (prev_median + median) / 2
        return median

