# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/?envType=problem-list-v2&envId=depth-first-search
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        curr = ''
        depth = 0
        maxDepth = 0
        for c in traversal:
            if c.isdigit():
                curr += c
            else:
                if curr:
                    nodes.append((TreeNode(int(curr)), depth))
                    curr = ''
                    depth = 1
                else:
                    depth += 1
                maxDepth = max(maxDepth, depth)
        if curr:
            nodes.append((TreeNode(int(curr)), depth))

        root = nodes[0][0]
        visited = [0] * (maxDepth + 1)
        for node, depth in nodes:
            visited[depth] = node
            if depth > 0:
                if visited[depth - 1].left == None:
                    visited[depth - 1].left = node
                else:
                    visited[depth - 1].right = node
        return visited[0]
