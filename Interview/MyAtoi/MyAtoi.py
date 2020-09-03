import sys


class Solution:
    def myAtoi(self, str: str) -> int:
        digit, num = 0, 0
        is_negative = False
        for i in str:
            if i in "+-" and digit == 0:
                is_negative = i == "-"
                digit += 1
            elif i in "0123456789":
                d = ord(i) - ord('0')
                if not is_negative and (2147483647 - d) / 10 < num:
                    return 2147483647
                if is_negative and (-2147483648 + d) / 10 > -num:
                    return -2147483648
                num = num * 10 + d
                digit += 1
            elif i not in " \n" or digit != 0:
                break
        if digit == 0:
            return 0
        return -num if is_negative else num

