# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/?envType=problem-list-v2&envId=depth-first-search
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def traverse(gparent, parent, child):
            if gparent and parent and child:
                if gparent.val % 2 == 0:
                    return child.val + traverse(parent, child, child.left) + traverse(parent, child, child.right)
                else:
                    return traverse(parent, child, child.left) + traverse(parent, child, child.right)
            else:       
                return 0

        res = 0
        if root:
            if root.left:
                res += traverse(root, root.left, root.left.right)
                res += traverse(root, root.left, root.left.left)
            if root.right:
                res += traverse(root, root.right, root.right.right)
                res += traverse(root, root.right, root.right.left)
        
        return res
