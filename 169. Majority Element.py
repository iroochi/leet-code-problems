def majority_element(nums):
    number = 0
    count = 0

    # finding a number
    for i in nums:
        if count == 0:
            number = i
        if i == number:
            count += 1
        else:
            count -= 1
    
    # verifying the number
    count = 0
    for i in nums:
        if i == number:
            count += 1
    
    if count > len(nums) // 2:
        return number
    
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))