class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_key = {}
        for i, num in enumerate(nums):
            compute = target - num
            if compute in num_key:
                return [num_key[compute], i]
            num_key[num] = i