# https://leetcode.com/problems/h-index/description/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0
