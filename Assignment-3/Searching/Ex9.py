from collections import deque
def get_index(char):
        return ord(char) - ord('a')

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
  
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            index = get_index(char)
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end = True

    def search(self, word):
        current = self.root
        for char in word:
            index = self._get_index(char)
            if not current.children[index]:
                return False
            current = current.children[index]

# Given an array of strings arr[] 
# and some queries where each query consists of a string str and an integer k.
# The task is to find the count of strings in arr[] 
# whose prefix of length k matches with the k length prefix of str.

# Input: arr[] = {"abba", "abbb", "abbc", "abbd", "abaa", "abca"}, 
#      str   = "abbg", 
#      k     = 3
# Output: 4

def count_matches(arr, str, k):
    trie = Trie()
    for string in arr:
        trie.insert(string)

    current = trie.root
    count = 0
    for char in str[:k]:
        index = get_index(char)
        if not current.children[index]:
            return count
        current = current.children[index]

    queue = deque([current])
    while queue:
        current = queue.popleft()
        if current.is_end:
            count += 1
        for child in current.children:
            if child:
                queue.append(child)
                    
    return count

print(count_matches(["abba", "abbb", "abbc", "abbd", "abaa", "abca"], "abbg", 3))
print(count_matches(["abba", "abbb", "abbc", "abbd", "abaa", "abca"], "abbg", 2))
print(count_matches(["abba", "abbb", "abbc", "abbd", "abaa", "abca"], "abbg", 4))
print(count_matches(["abbac", "abbbc", "abbc", "abb", "abaa", "abc"], "abbg", 3))
print(count_matches(["abbac", "abbbc", "abbc", "abb", "abaa", "ab"], "abbg", 3))