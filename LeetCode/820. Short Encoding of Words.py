# 820. Short Encoding of Words
# https://leetcode.com/problems/short-encoding-of-words/
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
# Input: words = ["t"]
# Output: 2
# Explanation: A valid encoding would be s = "t#" and indices = [0]

class Node:
    def __init__(self):
        self.edges = {}

    def addEdge(self, c):
        if c not in self.edges:
            self.edges[c] = Node()
        return self.getEdge(c)
    
    def getEdge(self, c):
        if c not in self.edges:
            return None
        return self.edges[c]
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word):
        current = self.root
        
        for c in word:
            current = current.addEdge(c)
            
    def findPrefix(self, word):
        current = self.root
        
        for c in word:
            current = current.getEdge(c)
            if current is None:
                return False
        return True

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda word: -len(word))
        trie = Trie()
        ans = 0   
    
        for word in [w[::-1] for w in words]:
            if not trie.findPrefix(word):
                trie.addWord(word)
                ans += len(word) + 1
        return ans