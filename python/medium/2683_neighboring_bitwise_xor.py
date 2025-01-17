# https://leetcode.com/problems/neighboring-bitwise-xor/description/?envType=daily-question&envId=2025-01-17
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not derived.count(1) % 2
        # sum = 0
        # for n in derived:
        #     sum = sum ^ n
        
        # return sum == 0
