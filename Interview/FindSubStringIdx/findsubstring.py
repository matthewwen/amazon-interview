from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result_indices = []

        if len(words) == 0:
            return []

        const_len = len(words[0])
        words_map = Counter(words)

        for i, _ in enumerate(s):
            temp_word = s[i: i + const_len]
            if len(temp_word) != const_len:
                break
            if temp_word in words_map:
                copy_map = words_map.copy()
                for y in range(i, len(s), const_len):
                    words_after_temp = s[y: y + const_len]
                    if words_after_temp in copy_map and copy_map[words_after_temp] != 0:
                        copy_map[words_after_temp] -= 1
                    else:
                        break

                is_clear = True
                for k, v in copy_map.items():
                    is_clear = is_clear and v == 0

                if is_clear:
                    result_indices.append(i)

        return result_indices
