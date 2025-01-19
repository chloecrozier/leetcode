# https://leetcode.com/problems/add-to-array-form-of-integer/description/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if len(str(k)) > len(num):
            temp = k
            k = int(''.join(map(str, num)))
            num = [int(n) for n in str(temp)]
        
        carry = 0
        i = len(num) - 1
        res = []
        while k:
            sumVal = carry + (k % 10) + num[i]
            if sumVal >= 10:
                carry = 1
            else:
                carry = 0
            res.insert(0, sumVal % 10)
            i -= 1
            k = k // 10

        while i >= 0:
            sumVal = carry + num[i]
            if sumVal >= 10:
                carry = 1
            else:
                carry = 0
            res.insert(0, sumVal % 10)
            i -= 1

        if carry:
            res.insert(0, 1)

        return res
        # return [int(x) for x in list(str(int(''.join(map(str, num))) + k))] 
