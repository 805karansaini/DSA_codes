# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes
# before the intersected node in A; There are 3 nodes before the intersected


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummy1 = inter1 = headA
        dummy2 = inter2 = headB

        while dummy1 and dummy2:
            dummy1 = dummy1.next
            dummy2 = dummy2.next

        if dummy1:
            while dummy1:
                inter1 = inter1.next
                dummy1 = dummy1.next
        elif dummy2:
            while dummy2:
                inter2 = inter2.next
                dummy2 = dummy2.next

        while inter1 and inter2:
            if inter1 == inter2:
                return inter1
            else:
                inter1 = inter1.next
                inter2 = inter2.next
        return None