class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = []
        for a, b in zip(word1, word2):
            res.extend([a, b])
        return "".join(res) + word1[n:] + word2[m:]
