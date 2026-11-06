# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    def minHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + min(self.maxHeight(root.left), self.maxHeight(root.right))
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        maxLeaf = self.maxHeight(root)
        minLeaf = self.minHeight(root)
        
        return maxLeaf - minLeaf <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)