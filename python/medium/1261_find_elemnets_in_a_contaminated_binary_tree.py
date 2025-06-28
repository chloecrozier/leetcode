# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()

        toVisit = [root]
        root.val = 0
        self.seen.add(root.val)

        while toVisit:
            curr = toVisit.pop(0)
            self.seen.add(curr.val)
            if curr.left:
                curr.left.val = (curr.val * 2) + 1
                toVisit.append(curr.left)
            if curr.right:
                curr.right.val = (curr.val * 2) + 2
                toVisit.append(curr.right)

    def find(self, target: int) -> bool:
        if target in self.seen:
            return True
        else:
            return False
