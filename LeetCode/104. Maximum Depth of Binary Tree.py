# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global best
        best = 0

        def rec(root, length):
            global best
            if not root.left:
                best = max(best, length)
            if not root.right:
                best = max(best, length)
            if root.left:
                rec(root.left, length + 1)
            if root.right:
                rec(root.right, length + 1)

        if root:
            rec(root, 1)

        return best
