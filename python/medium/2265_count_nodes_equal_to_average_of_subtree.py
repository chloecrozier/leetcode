# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/?envType=problem-list-v2&envId=depth-first-search
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def traverse(root):
            if root:
                leftRes, leftSum, leftCount = traverse(root.left)
                rightRes, rightSum, rightCount = traverse(root.right)
                res = leftRes + rightRes
                sum = leftSum + rightSum
                count = leftCount + rightCount
                if root.val == (root.val + sum) // (count + 1):
                    return res + 1, sum + root.val, count + 1 
                else:
                    return res + 0, sum + root.val, count + 1 
            else:
                return 0, 0, 0

        return traverse(root)[0]
