# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.search(root)
        return res[0]
    # Search return max profit stolen at root 
    # and money from node.left and node.right
    def search(self, root):
        if root is None:
            return (0,0)
        left = self.search(root.left)
        right = self.search(root.right)
        res = max(root.val + left[1] + right[1], left[0] + right[0])
        return (res, left[0] + right[0])
    