# https://leetcode.com/problems/find-bottom-left-tree-value/description/
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        maxDepth = -1
        left = root.val
        
        def getDepth(root: TreeNode, currDepth: int):
            if root != None:
                nonlocal left, maxDepth
                if maxDepth < currDepth:
                    maxDepth = currDepth
                    left = root.val
                getDepth(root.left, currDepth + 1)
                getDepth(root.right, currDepth + 1)

        getDepth(root, 1)
        return left
