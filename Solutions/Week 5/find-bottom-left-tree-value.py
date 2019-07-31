# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.ans = [0, 0] 
        self.helper(root, 1)
        return self.ans[0]
    
    def helper(self, root, floor):
        if not root:
            return
        if (floor>self.ans[1]):
            self.ans[0] = root.val
            self.ans[1] = floor
        self.helper(root.left, floor+1)
        self.helper(root.right, floor+1)
