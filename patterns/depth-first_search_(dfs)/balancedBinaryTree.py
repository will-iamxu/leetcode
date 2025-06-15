# Bottom up recursive DFS
# goes to bottom node and tracks height of each node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def height(root):
            if not root:
                return 0
            left, right = height(root.left), height(root.right)
            if abs(left-right) > 1:
                self.bal = False
                return 0
            return 1 + max(left, right)
        height(root)
        return self.bal
