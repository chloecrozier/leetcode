# https://leetcode.com/problems/count-symmetric-integers/description/?envType=daily-question&envId=2025-04-11
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            curr = [int(x) for x in str(i)]
            length = len(curr)
            if length % 2 == 0:
                halfLen = length // 2
                if sum(curr[0:halfLen]) == sum(curr[halfLen:]):
                    count += 1
        return count
