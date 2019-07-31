# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.helper(root.left)+self.helper(root.right), max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
    
    def helper(self, root):
        if not root:
            return 0
        return 1+max(self.helper(root.left), self.helper(root.right))