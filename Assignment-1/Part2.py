def isStringPermutation(s1: str, s2: str) -> bool:
    letters = {} 
    for letter in s1: # O(n)
        if letter in letters: # O(1)
            letters[letter] += 1 # O(1)
        else:
            letters[letter] = 1 # O(1)
    # O(n) space

    for letter in s2: # O(n)
        if letter in letters: # O(1)
            letters[letter] -= 1 # O(1)
            if letters[letter] == 0: # O(1)
                del letters[letter] # O(1)
        else:
            return False # O(1)

    return len(letters) == 0 # O(n)

# Time: O(n)
# Space: O(n)

print(isStringPermutation('asdf', 'fsda'))
print(isStringPermutation('asdf', 'fsa'))
print(isStringPermutation('asdf', 'fsax'))

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    num_set = set(inputArray) # O(n) time and space
    result = [] # O(n) space
    for num in inputArray: # O(n)
        if (targetSum - num) in num_set: # O(1)
            result.append((num, targetSum - num)) # O(1)
        num_set.remove(num) # O(1)
    return result

# Time: O(n)
# Space: O(n)

print(pairsThatEqualSum([1, 2, 3, 4, 5], 5))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7))