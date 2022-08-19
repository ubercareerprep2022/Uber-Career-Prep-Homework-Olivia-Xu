def group_anagrams(words):
    groups = {}
    for word in words:
        count = {}
        for char in word:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        # frozenset takes an iterable object as input and makes them immutable.
        key = frozenset(count)
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    result = []
    for group in groups.values():
        result.extend(group)
    return result

words = ["cat", "dog", "tac", "god", "act"]
print(group_anagrams(words))
words = ["caat", "dog", "atac", "god", "acta"]
print(group_anagrams(words))
words = ["cat", "", "tac", "god", "act"]
print(group_anagrams(words))
words = []
print(group_anagrams(words))
words = ['']
print(group_anagrams(words))