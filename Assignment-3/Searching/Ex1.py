# Write the code to find the minimum element in a rotated and sorted array
def find_min(nums):
    if not nums: return None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return nums[i+1]
    return nums[0]

print(find_min([]))
print(find_min([4,5,6,7,9,2,3]))
print(find_min([1,2,3,4,5]))
print(find_min([5,1,2,3,4]))
print(find_min([1]))