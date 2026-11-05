# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = []
        while head is not None:
            node.append(head)
            head = head.next

        r = len(node)-1
        l = 0
        j = 0

        while l<r:
            if j % 2 == 0:
                node[l].next = node[r]
                l+=1
            else:
                node[r].next = node[l]
                r-=1
            j+=1
        node[r].next = None




        