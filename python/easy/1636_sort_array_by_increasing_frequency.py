# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        freq = sorted(freq.items(), key=lambda x: (x[1], -x[0]))
        for key, val in freq:
            for i in range(val):
                res.append(key)
        return res
