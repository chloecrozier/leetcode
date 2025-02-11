# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
class Solution:
    currSum = 0

    def traverse(self, root):
        if root:
            self.traverse(root.right)
            self.currSum += root.val
            root.val = self.currSum
            self.traverse(root.left)

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
