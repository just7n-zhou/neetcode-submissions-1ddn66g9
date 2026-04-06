# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndx = inIndx = 0 
        def dfs(limit):
            nonlocal preIndx, inIndx 
            if preIndx >= len(preorder):
                return None 
            if inorder[inIndx] == limit:
                inIndx += 1 
                return None 
            
            root = TreeNode(preorder[preIndx])
            preIndx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root 
        
        return dfs(float('inf'))