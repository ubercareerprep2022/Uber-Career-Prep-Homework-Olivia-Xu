def sorted_merge(arrA, arrB):
    p1 = arrA.index(None) -1
    p2 = len(arrB) -1
    p3 = p1 + p2 + 1
    if p1 == -1:
            arrA[:p2] = arrB[:p2]
    while p1 >= 0 and p2 >= 0:
        if arrA[p1] > arrB[p2]:
            arrA[p3] = arrA[p1]
            p1 -= 1
        else:
            arrA[p3] = arrB[p2]
            p2 -= 1
        p3 -= 1
        if p1 == -1:
            arrA[:p2] = arrB[:p2]

# Given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B
a = [10, 12, 13, 14, 18, None, None, None, None, None, None]
b = [16, 17, 19, 20, 22]
sorted_merge(a, b)
print(a)

a = [10, 12, 13, 14, 18, None, None, None, None, None, None]
b = [16, 17, 19, 20, 22, 24]
sorted_merge(a, b)
print(a)

a = [10, 10, 16, None, None, None, None, None, None]
b = [10, 16, 19, 20, 22]
sorted_merge(a, b)
print(a)

a = [None, None, None, None, None, None]
b = [10, 16, 19, 20, 22]
sorted_merge(a, b)
print(a)
    