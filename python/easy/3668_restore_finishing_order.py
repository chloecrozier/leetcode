# https://leetcode.com/problems/restore-finishing-order/description/
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        friends = set(friends)
        for num in order:
            if num in friends:
                res.append(num)
        return res
