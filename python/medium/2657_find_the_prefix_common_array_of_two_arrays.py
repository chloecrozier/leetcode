# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2025-01-14
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = [0] * len(A)
        res = []
        curr = 0
        for i in range(len(A)):
            count[A[i] - 1] += 1
            count[B[i] - 1] += 1
            if A[i] == B[i]:
                if count[A[i] - 1] == 2:
                    curr += 1
            else:
                if count[A[i] - 1] == 2:
                    curr += 1
                if count[B[i] - 1] == 2:
                    curr += 1
            res.append(curr)
        return res
