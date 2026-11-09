# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodeLen = 0
        curr = head
        while curr is not None:
            curr = curr.next
            nodeLen+=1
        print(nodeLen)
        AnsP = nodeLen - n
        print(AnsP)
        if AnsP == 0:
            return head.next

        curr = head
        for i in range(AnsP):
            if (i+1) == AnsP:
                curr.next = curr.next.next
                return head
            curr = curr.next


