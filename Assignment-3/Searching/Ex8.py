# Given an array of size n and an integer k, 
# return the count of distinct numbers in all windows of size k.

def distinct_num(arr, k):
    # maintain a sliding window of size k
    # using the first window to initialize a dictionary
    # and a count_distinct that denotes the length of the dictionary

    # when updating the window
    # decrement in the dict the count of the number that will be excluded
    # if the count reaches zero, decrement count_distinct
    # for the incoming number
    # if it doesn't exist in the dictionary, add it to the dictionary
    # and increment count_distinct
    # for each window, append count_distinct to a result array

    arr_dict = {}
    count_distinct = 0
    for num in arr[:k]:
        if num not in arr_dict:
            arr_dict[num] = 1
            count_distinct += 1
        else:
            arr_dict[num] += 1
    
    result = [count_distinct]

    left, right = 0, k
    while right < len(arr):
        arr_dict[arr[left]] -= 1
        if arr_dict[arr[left]] == 0:
            count_distinct -= 1
            del arr_dict[arr[left]]
        if arr[right] not in arr_dict:
            arr_dict[arr[right]] = 1
            count_distinct += 1
        else:
            arr_dict[arr[right]] += 1
        left += 1
        right += 1
        result.append(count_distinct)

    return result

print(distinct_num([1, 2, 1, 3, 4, 2, 3], 4))
print(distinct_num([1, 2, 4, 4], 2))
print(distinct_num([1, 2, 4, 4], 1))