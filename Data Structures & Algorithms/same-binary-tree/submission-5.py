# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            qNode, pNode = stack.pop()

            if not qNode and not pNode:
                continue 
            if not qNode or not pNode:
                return False 
            if qNode.val != pNode.val:
                return False 
            
            stack.append((qNode.left, pNode.left))
            stack.append((qNode.right, pNode.right))
        
        return True 
            
