class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            res.append(nums[i]*nums[i])
        res.sort()
        return res