# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 1
        self.helper(root)
        return self.ans-1
        
    def helper(self, root):
        if not root:
            return 0
        # if not root.left and not root.right:
            # return 
        left = 0
        right = 0
        if root.left and root.val == root.left.val:
            left = 1+self.helper(root.left)
        elif root.left:
            left = 0*self.helper(root.left)
        if root.right and root.val == root.right.val:
            right = 1+self.helper(root.right)
        elif root.right:
            right = 0*self.helper(root.right)
        if root.left and root.left.val == root.val and root.right and root.right.val == root.val:
            self.ans = max(self.ans, left+right+1)
        else:
            self.ans = max(self.ans, max(left, right)+1)
        return max(left, right)
