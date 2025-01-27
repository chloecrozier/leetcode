# https://leetcode.com/problems/count-complete-tree-nodes/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left and root.right:
                return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            elif root.left:
                return 1 + self.countNodes(root.left)
            elif root.right:
                return 1 + self.countNodes(root.right)
            else:
                return 1
        else:
            return 0
