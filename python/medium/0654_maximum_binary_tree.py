# https://leetcode.com/problems/maximum-binary-tree/description/
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(ls):
            if ls:
                curr = TreeNode(max(ls))
                i = ls.index(curr.val)
                curr.left = build(ls[0:i])
                curr.right = build(ls[i + 1:])
                return curr
            else:
                return None

        root = TreeNode(max(nums))
        i = nums.index(root.val)
        root.left = build(nums[0:i])
        root.right = build(nums[i + 1:])

        return root
