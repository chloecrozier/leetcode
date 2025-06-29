# https://leetcode.com/problems/maximum-binary-tree/description/
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # def addNode(val, curr):
        nums.sort()

        root = TreeNode(nums.pop())
        curr = root
        while nums:
            addNode(nums.pop(), curr)
            addNode(nums.pop(), curr)
        
        return root
