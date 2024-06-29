class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        position = 0
        count = 0
        for num in nums:
            if count == 0:
                position = num
            count += (1 if num == position else -1)
        
        count = 0
        for num in nums:
            if num == position:
                count += 1
        
        if count > len(nums) // 2:
            return position
