# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/?envType=daily-question&envId=2025-06-07
class Solution:
    def clearStars(self, s: str) -> str:
        pq = []
        temp = list(s)
        for i in range(len(s)):
            if s[i] == '*':
                temp[i] = '0'
                min = heappop(pq)
                temp[-min[1]] = '0'
            else:
                heappush(pq, (s[i], -i))
        return ''.join(c for c in temp if c!= '0')
