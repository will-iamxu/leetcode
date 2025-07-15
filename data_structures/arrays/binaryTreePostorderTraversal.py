# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        #left -> right -> node
        def postOrder(node):
            if not node:
                return None
            postOrder(node.left)
            postOrder(node.right)
            res.append(node.val)
        postOrder(root)
        return res 