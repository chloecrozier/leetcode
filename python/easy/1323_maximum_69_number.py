# https://leetcode.com/problems/maximum-69-number/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def maximum69Number (self, num: int) -> int:
        numArr = [int(c) for c in str(num)]
        sixToNine = num
        nineToSix = num

        for i in range(len(numArr)):
            if numArr[i] == 6:
                numArr[i] = 9
                sixToNine = int("".join(map(str, numArr)))
                numArr[i] = 6
                break

        for i in range(len(numArr) - 1, -1, -1):
            if numArr[i] == 9:
                numArr[i] = 6
                nineToSix  = int("".join(map(str, numArr)))
                numArr[i] = 9
                break

        return max(sixToNine, nineToSix)
