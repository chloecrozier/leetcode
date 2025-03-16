# https://leetcode.com/problems/minimum-time-to-repair-cars/description/?envType=daily-question&envId=2025-03-16
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def canRepair(time):
            count = 0
            for r in ranks:
                n = isqrt(time // r)
                if n <= time:
                    count += n
            return count

        l = 1
        r = max(ranks) * cars * cars

        while l < r:
            mid = (l + r) // 2
            if canRepair(mid) >= cars:
                r = mid
            else:
                l = mid + 1
        
        return l
