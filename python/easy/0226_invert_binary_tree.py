# https://leetcode.com/problems/invert-binary-tree/description/
class Solution:
    def swapChildren(self, root: Optional[TreeNode]):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.swapChildren(root.left)
            self.swapChildren(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.swapChildren(root)
        return root
