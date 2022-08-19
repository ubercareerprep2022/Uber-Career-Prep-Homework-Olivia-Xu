def peaks_valleys(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        elif i < len(nums) - 2 and nums[i + 2] < nums[i + 1]:
            nums[i + 2], nums[i + 1] = nums[i + 1], nums[i + 2]
        i += 2

    return nums

nums = [5, 3, 1, 2, 3]
peaks_valleys(nums)
print(nums)
nums = [5, 3, 1, 0, 2, 3]
peaks_valleys(nums)
print(nums)
nums = []
peaks_valleys(nums)
print(nums)
nums = [1]
peaks_valleys(nums)
print(nums)