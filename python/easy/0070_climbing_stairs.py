# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
    
        prevPrevStep = 1
        prevStep = 2
        permutations = 0
        for i in range(3, n + 1):
            permutations = prevPrevStep + prevStep
            prevPrevStep = prevStep
            prevStep = permutations

        return permutations
