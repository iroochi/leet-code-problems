class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lth = 0
        modified_s = s.strip()

        for i in range(len(modified_s)):
            if modified_s[i] == " ":
                lth = 0
            else:
                lth += 1
        return lth