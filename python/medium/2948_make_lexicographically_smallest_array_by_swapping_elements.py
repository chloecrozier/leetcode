# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/?envType=daily-question&envId=2025-01-25
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        res = [0] * len(nums)
        listPairs = []
        for i in range(len(nums)):
            listPairs.append((nums[i], i))

        sortedPairs = sorted(listPairs, key=lambda x: x[0])
    
        groups = [[sortedPairs[0]]]
        for i in range(1, len(sortedPairs)):
            prev = sortedPairs[i - 1]
            curr = sortedPairs[i]
            if curr[0] - prev[0] <= limit:
                groups[-1].append(curr)
            else:
                groups.append([curr])

        for group in groups:
            pq = []
            for val, i in group:
                heapq.heappush(pq, i)
            for i in range(len(pq)):
                res[heapq.heappop(pq)] = group[i][0]

        return res
