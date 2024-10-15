class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = []
        w2 = []
        for i in range(len(word1)):
            w1 = "".join(word1)
        for j in range(len(word2)):
            w2 = "".join(word2)
        if w1 == w2:
            return True
        return False

