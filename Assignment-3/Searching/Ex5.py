def seach_matrix(val, matrix):
    if not matrix: return False
    row, col = len(matrix), len(matrix[0])

    # traverse the matrix diagonally
    # until the currrent num is greater than val
    # visit the numbers in the row and col of that current num
    # from right to left, bottom to top, starting from current num
    # stop when found a num <= val
    # if equal, return true
    # if not found in both directions, return false
    # when traversing diagonally, if hit the border, then start going horizontally/vertically
    # if going vertically, then only visit the nums in the row
    # if going horizonaly, then only visit the nums in the col

    i, j = 0, 0
    while i < row or j < col:
        if i == row:
            if matrix[i-1][j] < val:
                j += 1
            else:
                while j >= 0 and matrix[i-1][j] >= val:
                    if matrix[i-1][j] == val:  
                        return True
                    j -= 1
                return False
        elif j == col:
            if matrix[i][j-1] < val:
                i += 1
            else:
                while i >= 0 and matrix[i][j-1] >= val:
                    if matrix[i][j-1] == val:  
                        return True
                    i -= 1
                return False
        else:
            if matrix[i][j] < val:
                i +=1
                j += 1
            elif matrix[i][j] == val:
                return True
            else:
                temp_i, temp_j = i - 1, j - 1
                while temp_i >= 0 and matrix[temp_i][j] >= val:
                    if matrix[temp_i][j] == val:
                        return True
                    temp_i -= 1
                while temp_j >= 0 and matrix[i][temp_j] >= val:
                    if matrix[i][temp_j] == val:
                        return True
                    temp_j -= 1
                return False
    return False

print(seach_matrix(5, [ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
))
print(seach_matrix(20, [ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
))

print(seach_matrix(200, [ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
))

print(seach_matrix(20, [ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],]
))

print(seach_matrix(20, [ [1,   4,  7, 11],
  [2,   5,  8, 12],
  [3,   6,  9, 16],
  [10, 13, 14, 17],
  [18, 21, 23, 26]]
))

print(seach_matrix(12, [ [1,   4,  7, 11],
  [2,   5,  8, 12],
  [3,   6,  9, 16],
  [10, 13, 14, 17],
  [18, 21, 23, 26]]
))