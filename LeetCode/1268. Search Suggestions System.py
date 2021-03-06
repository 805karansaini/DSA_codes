# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"] ]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        N = len(products)
        n = len(searchWord)
        dic = defaultdict(list)
        flag = True
        for i in range(n):
            c = 0
            temp = []
            j = 0
            while c < 3 and j < N and flag: # due to flag time taken reduced by 10 fold
                if products[j].startswith(searchWord[:i+1]):
                    temp.append(products[j])
                    c += 1
                j += 1
            if len(temp)==0:
                flag = False # set flag as Flase and always append a empty list to res
            res.append(temp)
        return res