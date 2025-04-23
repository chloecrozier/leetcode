# https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def getDigitSum(n):
            sum = 0
            while n:
                sum += n % 10
                n //= 10
            return sum
        
        m = {}
        count = 0
        maxVal = 0
        for i in range(1, n + 1):
            sum = getDigitSum(i)
            if sum in m:
                m[sum] += 1
            else:
                m[sum] = 1
            if m[sum] > maxVal:
                maxVal = m[sum]
                count = 1
            elif maxVal == m[sum]:
                count += 1
            
        return count
