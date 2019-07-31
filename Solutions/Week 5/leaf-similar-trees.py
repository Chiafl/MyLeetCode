# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leafSeq(root1)==self.leafSeq(root2)
    
    def leafSeq(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.leafSeq(root.left)+self.leafSeq(root.right)