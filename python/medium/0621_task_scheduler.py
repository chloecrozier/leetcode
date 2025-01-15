# https://leetcode.com/problems/task-scheduler/description/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        intervals = 0
        for c in tasks:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        pq = []
        for key, value in count.items():
            heapq.heappush(pq, (-value, key))
        
        seen = []
        putBack = []
        while pq or seen:
            if pq:
                task = heapq.heappop(pq)
            
                if (task[0], task[1]) in seen:
                    seen.append("idle")
                else:
                    seen.append((task[0] + 1, task[1]))
            else:
                seen.append("idle")

            if len(seen) > n:
                if seen[0] != "idle":
                    if seen[0][0] <= -1:
                        heapq.heappush(pq, (seen[0][0], seen[0][1]))
                seen = seen[1:]

            intervals += 1
            if not pq and seen.count("idle") == n:
                return intervals - n

        return intervals
