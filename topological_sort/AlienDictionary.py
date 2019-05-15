class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def compare_words(self, w1, w2):
        n = min(len(w1), len(w2))
        for i in range(n):
            c1 = w1[i]
            c2 = w2[i]
            if c1 != c2:
                return c1, c2

    def alienOrder(self, words):
        # Write your code here

        if len(words) in [0, 1]:
            return ""
        char_set = {}
        pairs = set()
        for word in words:
            for c in word:
                char_set.setdefault(c, 0)
        for i in range(0, len(words) - 1):
            c1, c2 = self.compare_words(words[i], words[i + 1])
            char_set[c2] += 1
            pairs.add((c1, c2))
        tmp = []
        result = ""
        for c in char_set:
            if char_set[c] == 0:
                tmp.append(c)
                result += c
        while tmp:
            c = tmp.pop(0)
            for p in pairs:
                c0, c1 = p
                if c0 == c:
                    char_set[c1] -= 1
                    if char_set[c1] == 0:
                        result += c1
                        tmp.append(c1)
        return result if len(result) == len(char_set.keys()) else ""


if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(Solution().alienOrder(words))
