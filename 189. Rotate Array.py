def rotate_array(nums, k):
    n = len(nums)
    k = k % n # normalizing the value of k
    nums.reverse() # reversing the whole array
    nums[:k] = reversed(nums[:k]) # reversed the first k elements in the reversed array
    nums[k:] = reversed(nums[k:]) # reversed the rest of the elements


nums = [1,2,3,4,5,6,7]
k = 3
rotate_array(nums, k)
print(nums)