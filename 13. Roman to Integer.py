class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nums = 0
        for char in range(len(s)-1):
            if roman[s[char]] < roman[s[char+1]]:
                nums -= roman[s[char]]
            else:
                nums += roman[s[char]]
        
        nums += roman[s[-1]]

        return nums