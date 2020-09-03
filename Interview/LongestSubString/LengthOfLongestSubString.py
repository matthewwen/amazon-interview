class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m, start = 0, 0
        window = set()

        issue = False
        for i in s:
            if i in window:
                m = len(window) if m < len(window) else m
                while i in window:
                    if start >= len(s):
                        issue = True
                        break
                    window.remove(s[start])
                    start += 1
                if issue:
                    break
            window.add(i)
        if not issue:
            m = len(window) if m < len(window) else m
        return m
