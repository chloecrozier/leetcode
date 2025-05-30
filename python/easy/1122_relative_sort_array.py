# https://leetcode.com/problems/relative-sort-array/description/?envType=problem-list-v2&envId=counting-sort
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * (max(arr1) + 1)
        for num in arr1:
            count[num] += 1
        print(count)

        res = []
        curr = 0
        val = 0
        for i in range(len(arr2)):
            for j in range(count[arr2[i]]):
                res.append(arr2[i])
            count[arr2[i]] = 0

        for i in range(len(count)):
            for j in range(count[i]):
                res.append(i)

        return res
