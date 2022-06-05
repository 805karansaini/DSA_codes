# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Input: n = 1
# Output: ["()"]

# add generated parenthesis to res[] GLOBAL VARIABLE
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(p,start,end):
            if start == n and end == n:
                res.append(p)
                return
            if start < n:
                generate(p + "(",start+1,end)
            if end < start and end < n:
                generate(p+")",start,end+1)
        generate("(",1,0)
        return res

# returns list of all the generated parenthesis
class Solution:
    def generateParenthesisRETURN(self, n: int) -> List[str]:
        first = ""
        second = ""

        def generate(p, start, end):
            first = []
            second = []
            if start == n and end == n:
                lis = []
                lis.append(p)
                return lis

            if start < n:
                first = generate(p + "(", start + 1, end)
            if end < start and end < n:
                second = generate(p + ")", start, end + 1)
            first = first + second
            return first

        return generate("", 0, 0)