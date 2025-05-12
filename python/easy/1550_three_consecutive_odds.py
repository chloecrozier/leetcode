# https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2025-05-11
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i + 2] % 2 == 0:
                i += 2
            elif arr[i + 1] % 2 == 0:
                i += 1
            elif arr[i] % 2:
                return True
        return False
