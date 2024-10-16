class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        split_s = len(s) // 2
        a = s[:split_s]
        b = s[split_s:]
        vowels = set('aeiouAEIOU')
        count_a = sum(1 for char in a if char in vowels)
        count_b = sum(1 for char in b if char in vowels)
        return count_a == count_b
