# https://leetcode.com/problems/height-checker/description/?envType=problem-list-v2&envId=counting-sort
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * (max(heights) + 1)
        res = 0
        for i in range(len(heights)):
            count[heights[i]] += 1
        
        val = 0
        curr = 0
        while curr < len(heights):
            for i in range(count[val]):
                if heights[curr] != val:
                    res += 1
                curr += 1
            val += 1

        return res
