# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        maxVal = root.val

        def search(root: TreeNode, maxVal: int):
            nonlocal count
            if root != None:
                if root.val >= maxVal:
                    maxVal = root.val
                    count += 1    

                search(root.left, maxVal)
                search(root.right, maxVal)
                
            return maxVal

        search(root, maxVal)
        return count
