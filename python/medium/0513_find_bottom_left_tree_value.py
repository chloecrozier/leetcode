# https://leetcode.com/problems/find-bottom-left-tree-value/description/
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        def getDepth(root: TreeNode):
            if root == None:
                return 0
            else:
                depth = max(getDepth(root.left), getDepth(root.right)) + 1
                return depth

        maxDepth = getDepth(root)
        lastRow = []

        def search(root: TreeNode, currDepth: int):
            if root != None:
                if currDepth == maxDepth:
                    lastRow.append(root.val)
                search(root.left, currDepth + 1)
                search(root.right, currDepth + 1)
        
        search(root, 1)
        return lastRow[0]
