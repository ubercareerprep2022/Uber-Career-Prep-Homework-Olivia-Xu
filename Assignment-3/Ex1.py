def three_partition_sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    i = 0
    while i < len(arr) and mid <= high:
        if arr[i] == 5:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            mid += 1
        elif arr[i] == 10:
            mid += 1
        elif arr[i] == 20:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
            i -= 1
        i += 1

test_arr = [5, 10, 5, 20, 5, 5, 10]
three_partition_sort(test_arr)
print(test_arr)
test_arr=[]
three_partition_sort(test_arr)
print(test_arr)
test_arr = [5, 10, 5, 10, 5, 5, 10]
three_partition_sort(test_arr)
print(test_arr)
test_arr = [5]
three_partition_sort(test_arr)
print(test_arr)