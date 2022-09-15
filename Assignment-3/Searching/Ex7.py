# Write a program that, 
# given an array A[] of n numbers and another number x, 
# determines whether or not there exist two elements in S whose sum is exactly x.

def has_sum(arr, x):
    arr_dict = {}
    for num in arr:
        if num not in arr_dict:
            arr_dict[num] = 1
        else:
            arr_dict[num] += 1

    for num in arr:
        arr_dict[num] -= 1
        if (x - num) in arr_dict and arr_dict[x-num] != 0:
            return True
    return False

print(has_sum([1,2,10,9,5], 6))
print(has_sum([1,2,10,9,5], 4))
print(has_sum([1,2,2,10,9,5], 4))