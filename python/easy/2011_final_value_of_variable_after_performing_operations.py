# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for operation in operations:
            if operation[1] == "-":
                x -= 1
            else:
                x += 1
        return x
