class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        ans[0] = self.search(nums, target, startIndex = True)
        ans[1] = self.search(nums, target, startIndex = False)
        return ans
    def search(self, nums: List[int], target: int, startIndex: bool) -> int:
        ans = -1
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                ans = mid
                if startIndex:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans