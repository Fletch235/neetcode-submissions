# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        lead = head
        
        for i in range(n):
            lead = lead.next
        
        while lead:
            left = left.next
            lead = lead.next


        left.next = left.next.next
        return dummy.next