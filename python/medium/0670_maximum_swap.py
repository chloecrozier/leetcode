# https://leetcode.com/problems/maximum-swap/description/?envType=daily-question&envId=2024-10-17
class Solution:
    def maximumSwap(self, num: int) -> int:
        ls = list(str(num))
        i = 0
        while i < len(ls) - 1 and ls[i + 1] <= ls[i]:
            i += 1

        maxVal = ls[i]
        maxIndex = i
        for j in range(i, len(ls)):
            if ls[j] >= maxVal:
                maxVal = ls[j]
                maxIndex = j

        k = 0
        while k < len(ls) - 1 and maxVal <= ls[k]:
            k += 1

        ls[k], ls[maxIndex] = ls[maxIndex], ls[k]

        return int(''.join(ls))
