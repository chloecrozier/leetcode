# https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2024-10-02
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = []
        valMap = {num: index + 1 for index, num in enumerate(sorted(set(arr[:])))}
        for num in arr:
            res.append(valMap[num])
        return res
