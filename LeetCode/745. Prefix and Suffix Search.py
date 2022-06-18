# 745. Prefix and Suffix Search
# https://leetcode.com/problems/prefix-and-suffix-search/


class WordFilter:

    def __init__(self, words: List[str]):
        self.lookup = {}
        
        for index, word in enumerate(words):
            for i in range(1, len(word) + 1):
                for j in range(1, len(word) + 1):
                    key = f"{word[:i]} {word[-j:]}"
                    self.lookup[key] = index

    def f(self, prefix: str, suffix: str) -> int:
        key = f"{prefix} {suffix}"
        
        if key in self.lookup:
            return self.lookup[key]
        return -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)