# https://leetcode.com/problems/valid-perfect-square/description/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        mid = ((r - l) // 2) + l + 1
        while mid != l:
            if num / mid == mid:
                return True
            elif num / mid > mid:
                l = mid
            else:
                r = mid
            mid = ((r - l) // 2) + l
        return False
