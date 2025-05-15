# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/?envType=daily-question&envId=2025-05-15
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        prev = groups[0]
        for i in range(1, len(words)):
            if prev != groups[i]:
                res.append(words[i])
                prev = groups[i]
        return res
