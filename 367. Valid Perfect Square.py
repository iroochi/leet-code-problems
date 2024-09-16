class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num == 0 or num == 1: 
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            root = mid * mid

            if root == num:
                return True
            elif root < num:
                left = mid + 1
            else:
                right = mid - 1
        return False