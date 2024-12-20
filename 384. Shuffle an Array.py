import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.nums_copy = nums[:]

    def reset(self) -> List[int]:
        self.nums_copy = self.nums[:]
        return self.nums_copy

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums_copy)-1, 0, -1):
            j = random.randint(0, i)
            self.nums_copy[i], self.nums_copy[j] = self.nums_copy[j], self.nums_copy[i]
        return self.nums_copy
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()