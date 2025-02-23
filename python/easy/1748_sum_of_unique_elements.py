# https://leetcode.com/problems/sum-of-unique-elements/description/
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = {}
        uniqueSum = 0
        for n in nums:
            if n in m:
                if m[n] == 1:
                    m[n] = 0
                    uniqueSum -= n
            else:
                m[n] = 1
                uniqueSum += n
        
        return uniqueSum
