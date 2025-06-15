# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/?envType=problem-list-v2&envId=depth-first-search
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ogVisit = [original]
        cpVisit = [cloned]
        while ogVisit and cpVisit:
            ogCurr = ogVisit.pop()
            cpCurr = cpVisit.pop()
            if ogCurr and cpCurr:
                if ogCurr == target:
                    return cpCurr
                ogVisit.append(ogCurr.right)
                ogVisit.append(ogCurr.left)
                cpVisit.append(cpCurr.right)
                cpVisit.append(cpCurr.left)
        return None
