# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/?envType=daily-question&envId=2025-03-14
class Solution:
    def isValid(self, ls, curr):
        count = 0
        for i in range(len(ls)):
            count += (ls[i] // curr)
        return count

    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        else:
            candies.sort()
            l = 1
            r = candies[-1]
            curr = l
            while l <= r:
                mid = (l + r) // 2
                count = self.isValid(candies, mid)
                if count < k:
                    r = mid - 1
                else:
                    curr = mid
                    l = mid + 1
        return curr
