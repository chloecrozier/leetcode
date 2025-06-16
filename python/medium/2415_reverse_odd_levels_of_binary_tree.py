# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/?envType=problem-list-v2&envId=depth-first-search
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(left, right, level):
            if left and right:
                if level % 2:
                    left.val, right.val = right.val, left.val
                traverse(left.left, right.right, level + 1)
                traverse(left.right, right.left, level + 1)

        traverse(root.left, root.right, 1)
        return root
