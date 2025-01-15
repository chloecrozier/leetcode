# https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-15
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = 0
        while num2:
            if num2 & 1:
                count += 1
            num2 = num2 >> 1

        res = []
        ones = 0
        n1 = bin(num1)[2:]

        for i in range(len(n1)):
            if n1[i] == '1':
                if ones < count:
                    res.append('1')
                    ones += 1
                else:
                    res.append('0')
            else:
                res.append('0')
            
        if ones == count:
            return int(''.join(res), 2)

        length = len(res) - 1
        while ones < count:
            print(length)
            if length > 0:
                if res[length] == '0':
                    res[length] = '1'
                    ones += 1
            else:
                res.append('1')
                ones += 1
            length -= 1

        return int(''.join(res), 2)
