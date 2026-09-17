# https://leetcode.com/problems/reorganize-string/submissions/2144352700/
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
            if freq[c] > ceil(len(s) / 2):
                return ""

        pq = []
        for key, val in freq.items():
            heapq.heappush(pq, (-val, key))

        res = ""
        lru = ''
        while pq:
            if res == "":
                nextFreq = heapq.heappop(pq)
                lru = nextFreq[1]
                res += nextFreq[1]
                if nextFreq[0] < -1:
                    heapq.heappush(pq, (nextFreq[0] + 1, nextFreq[1]))
            else:
                nextFreq = heapq.heappop(pq)
                backlog = []
                while nextFreq[1] == lru:
                    backlog.append(nextFreq)
                    nextFreq = heapq.heappop(pq)
                
                for entry in backlog:
                    heapq.heappush(pq, (entry[0], entry[1]))

                lru = nextFreq[1]
                res += nextFreq[1]
                if nextFreq[0] < -1:
                    heapq.heappush(pq, (nextFreq[0] + 1, nextFreq[1]))


        return res
