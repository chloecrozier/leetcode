# https://leetcode.com/problems/xbinary-tree-maximum-path-sum/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node:
            leftSum = max(0, self.dfs(node.left))
            rightSum = max(0, self.dfs(node.right))
            self.maxSum = max(self.maxSum, node.val + leftSum + rightSum)

            return max(leftSum, rightSum) + node.val
        else:
            return 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.dfs(root)
        return self.maxSum
