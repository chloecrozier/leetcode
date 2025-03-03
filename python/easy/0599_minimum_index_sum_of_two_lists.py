# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = {}
        res = []
        minSum = len(list1) + len(list2)
        currSum = 0
        for i in range(len(list1)):
            m[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in m:
                currSum = m[list2[i]] + i
                if currSum < minSum:
                    minSum = currSum
                    res = [list2[i]]
                elif currSum == minSum:
                    res.append(list2[i])

        return res
