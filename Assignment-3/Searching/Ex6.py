# Given two arrays: arr1[0..m-1] and arr2[0..n-1]. 
# Find whether arr2[] is a subset of arr1[] or not. 
# Both the arrays are not in sorted order. 
# It may be assumed that elements in both arrays are distinct.

def is_subset(arr1, arr2):
    # Assumption: len(arr2) <= len(arr1)
    arr1_set = set(arr1)

    for num in arr2:
        if num not in arr1_set:
            return False

    return True

print(is_subset([1,3,5,2,4,6], [2,6]))
print(is_subset([1,3,5,2,4,6], []))
print(is_subset([1,3,5,2,4,6], [2,6,7]))
print(is_subset([1,3,5,2,4,6], [1,3,5,2,4,6]))