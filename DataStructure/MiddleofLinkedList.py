
# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # while slow:
        #     if fast is None or fast.next is None:
        #         return slow
        #     else:
        #         fast = fast.next.next
        #     slow = slow.next
        #
        #
        # start = node = head
        # llen = 0
        # while start:
        #     llen += 1
        #     start = start.next
        #
        # middle = llen // 2
        # counter = 0
        #
        # while node:
        #     if counter == middle:
        #         return node
        #     else:
        #         counter += 1
        #         node = node.next

