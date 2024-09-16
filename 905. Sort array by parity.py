class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(1, len(nums)-i):
                if nums[j]%2 == 0 and nums[j-1]%2 != 0:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        
        return nums