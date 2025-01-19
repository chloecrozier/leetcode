# https://leetcode.com/problems/add-to-array-form-of-integer/description/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(x) for x in list(str(int(''.join(map(str, num))) + k))]
 
