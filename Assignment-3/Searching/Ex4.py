# There are two sorted arrays nums1 and nums2 of size m and n respectively. 
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)). 
# You may assume nums1 and nums2 cannot be both empty.

def find_median(l1, l2):
    if len(l1) > len(l2):
        return find_median(l2, l1)
    
    median_index = (len(l1) + len(l2) - 1) // 2
    is_even = ((len(l1) + len(l2) ) / 2 ) % 2

    start, end = 0, len(l1) - 1

    while start <= end:
        p1 = (start + end) // 2
        p2 = median_index - p1
        max_left_1, max_left_2 = l1[p1], l2[p2]
        if p1 == len(l1)-1:
            min_right_1 = float('inf')
        else:
            min_right_1 = l1[p1+1]  

        if p2 == len(l2)-1:
            min_right_2 = float('inf')
        else:
            min_right_2 = l2[p2+1]  
        
        if max_left_1 > min_right_2:
            end = p1 - 1
        elif max_left_2 > min_right_1:
            start = p1 + 1
        else:
            if is_even:
                return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2))/2
            else:
                return max(max_left_1, max_left_2)
    
print(find_median([1,2,3],[5,6]))
print(find_median([5,6],[1,2,3,4]))