def remove_duplicates(nums):
    if len(nums) == 0:
            return 0
    # keeping track of the position where the next unique or duplicate element will be placed
    j = 2 
    nums_size = len(nums)
    # loop starts with index 2 because the first 2 elements are always allowed because each unique element appears at most twice
    for i in range(2, nums_size): 
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1
    return j
    return nums[:j]
    

