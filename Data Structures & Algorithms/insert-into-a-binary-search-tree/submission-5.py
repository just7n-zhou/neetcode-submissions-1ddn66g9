# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Core idea:因为是二叉搜索树，所以插入的这个节点一定可以插入在叶子节点
        # 只需要找到对应的叶子节点然后根据val插入叶子节点左边或者右边
        if not root:
            return TreeNode(val)
        parent = None 
        cur = root 

        # 如果cur为none了，说明parent是叶子节点了
        while cur:
            parent = cur 
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        # 根据parent和val大小插入parent的左或者右
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root 