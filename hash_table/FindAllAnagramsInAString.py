# LC 438
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        n, m = len(s), len(p)
        p_str = Counter(p)
        cur_str = Counter(s[:m])
        if p_str == cur_str:
            result.append(0)
        for i in range(1, n - m + 1):
            new_char = s[i + m - 1]
            old_char = s[i - 1]
            cur_str[new_char] += 1
            cur_str[old_char] -= 1
            if cur_str[s[i - 1]] == 0:
                del cur_str[s[i - 1]]

            if p_str == cur_str:
                result.append(i)

        return result
