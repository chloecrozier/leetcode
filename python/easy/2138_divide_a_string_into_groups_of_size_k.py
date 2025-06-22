# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/?envType=daily-question&envId=2025-06-22
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        i = 0
        while i + k <= len(s):
            res.append(s[i:i + k])
            i += k

        if i < len(s):
            tail = [fill] * (k - len(s) - i)
            # print(i, s[i:] + ''.join(tail))
            res.append(s[i:] + ''.join(tail))
        return res
