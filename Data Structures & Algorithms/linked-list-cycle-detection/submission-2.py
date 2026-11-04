# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        fast = head.next

        while fast != head:

            head = head.next
            for i in range(2):
                if fast.next is None:
                    return False
                fast = fast.next

        return True