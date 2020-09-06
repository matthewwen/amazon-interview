from typing import List


class Solution:
    def matchPatterns(self, s, p, memo):
        if not p:
            return not s

        if (s, p) in memo:
            return memo[(s, p)]

        # Check if the first character matches
        first_char = True if s and p[0] in {s[0], '.'} else False

        # Check if the pattern has a '*'
        # Yes, then there are 2 possibilities,
        # 1. The pattern may not exist in the text eg: text = "aac" pattern='c*a'
        # 2. The pattern may exist in the text eg: text='cccccaaa' pattern = 'c*a*'
        # So call the matchPatterns twice by removing the first char from the string and keep
        # The pattern as is or remove the pattern and keep the string as is
        if len(p) >= 2 and p[1] == '*':
            memo[(s, p)] = self.matchPatterns(s, p[2:], memo) or (first_char and self.matchPatterns(s[1:], p, memo))
            return memo[(s, p)]
        else:
            # if the chars are a match then if there is no '*' remove the first chars
            # from the text and pattern and call matchPatterns again
            memo[(s, p)] = self.matchPatterns(s[1:], p[1:], memo) and first_char
            return memo[(s, p)]

    def isMatch(self, s: str, p: str) -> bool:
        return self.matchPatterns(s, p, {})
