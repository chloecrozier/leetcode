# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefix = [0] * len(boxes)
        count = int(boxes[0])
        for i in range(1, len(boxes)):
            prefix[i] = prefix[i - 1] + count
            count += int(boxes[i])

        postfix = [0] * len(boxes)
        count = int(boxes[-1])
        for i in range(len(boxes) - 2, -1, -1):
            postfix[i] = postfix[i + 1] + count
            count += int(boxes[i])
        
        res = []
        for i in range(len(boxes)):
            res.append(prefix[i] + postfix[i])
        return res
