# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/?envType=daily-question&envId=2025-03-04
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n //= 3
        return True
