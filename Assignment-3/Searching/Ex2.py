# Write the code to find an element in a rotated and sorted array

def find_element(num, nums):
    def same_side(num, mid, first):
        return (num < first) == (mid < first)

    r, l = len(nums) - 1, 0
    mid = (r + l) // 2
    while l <= r:
            if num > nums[mid]:
                if same_side(num, nums[mid], nums[l]):
                    l = mid + 1
                else:
                    r = mid - 1
            elif num < nums[mid]:
                if same_side(num, nums[mid], nums[l]):
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                return mid
            mid = (r + l) // 2

    return -1

print(find_element(2, [6,7,8,9,1,2]))
print(find_element(7, [6,7,8,9,1,2]))
print(find_element(6, [6,7,8,9,1,2]))
print(find_element(7, [6,7,8,9,1,2,3]))
print(find_element(3, [6,7,8,9,1,2,3]))
print(find_element(0, [6,7,8,9,1,2,3]))
print(find_element(0, [6]))
print(find_element(0, [0]))
print(find_element(0, []))


        

