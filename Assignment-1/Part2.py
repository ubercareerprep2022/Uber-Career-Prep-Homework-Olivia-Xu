def isStringPermutation(s1: str, s2: str) -> bool:
    letters = {}
    for letter in s1:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    for letter in s2:
        if letter in letters:
            letters[letter] -= 1
            if letters[letter] == 0:
                del letters[letter]
        else:
            return False
    return len(letters) == 0

print(isStringPermutation('asdf', 'fsda'))
print(isStringPermutation('asdf', 'fsa'))
print(isStringPermutation('asdf', 'fsax'))

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    num_set = set(inputArray)
    result = []
    for num in inputArray:
        if (targetSum - num) in num_set:
            result.append((num, targetSum - num))
        num_set.remove(num)
    return result

print(pairsThatEqualSum([1, 2, 3, 4, 5], 5))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7))