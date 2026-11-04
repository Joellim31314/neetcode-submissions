# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        if head == None:
            return False
        while head.next != None:
            #first compare will have null in set
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False