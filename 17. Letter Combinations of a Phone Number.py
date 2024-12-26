class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

        res = []
        def backtrack(index, curr_str):
            if index == len(digits):
                res.append(curr_str)
                return
            curr = digits[index]
            letters = digit_map[curr]
        
            for letter in letters:
                backtrack(index + 1, curr_str + letter)
        
        backtrack(0, "")

        return res