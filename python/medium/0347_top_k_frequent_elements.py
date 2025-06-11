# https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        return [y[0] for y in sorted(m.items(), key=lambda x: x[1], reverse=True)[:k]]
