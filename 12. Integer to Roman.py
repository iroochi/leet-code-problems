class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        int_to_roman = ""
        for i in range(len(integers)):
            while num >= integers[i]:
                int_to_roman = int_to_roman + romans[i]
                num = num - integers[i]
        
        return int_to_roman