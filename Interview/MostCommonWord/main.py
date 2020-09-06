from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        set_banned = set(banned)
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]', '\t', paragraph)
        words = paragraph.split()
        count_words = dict()
        for i in words:
            if i not in set_banned:
                if i in count_words:
                    count_words[i] = count_words[i] + 1
                else:
                    count_words[i] = 1

        count, word = 0, None
        for k, v in count_words.items():
            if v > count:
                count, word = v, k

        return word
