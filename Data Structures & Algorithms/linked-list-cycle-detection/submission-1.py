# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        visited = set()
        node = head
        while node.next:
            if node.next in visited:
                return True
            visited.add(node.next)
            node = node.next
        return False