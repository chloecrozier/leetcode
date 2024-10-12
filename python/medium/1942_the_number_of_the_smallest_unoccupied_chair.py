# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/?envType=daily-question&envId=2024-10-12
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrival = []
        leaving = []
        availableChairs = []
        occupiedChairs = {}

        for i in range(len(times)):
            heapq.heappush(arrival, (times[i][0], i))
            heapq.heappush(leaving, (times[i][1], i))

        for i in range(len(times)):
            heapq.heappush(availableChairs, i)
        
        while arrival:
            aTime, aIndex = heapq.heappop(arrival)
            
            while leaving and leaving[0][0] <= aTime:
                lTime, lIndex = heapq.heappop(leaving)
                heapq.heappush(availableChairs, occupiedChairs[lIndex])

            chair = heapq.heappop(availableChairs)
            occupiedChairs[aIndex] = chair

            if aIndex == targetFriend:
                return chair
        return -1
