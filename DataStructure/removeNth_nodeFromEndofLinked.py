# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r, l = head, head
        while n:
            n -= 1
            r = r.next
        if not r:
            l = l.next
            return l
        r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head




