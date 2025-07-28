# https://leetcode.com/problems/decode-xored-array/description/
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [0] * len(encoded)
        res[0] = first
        for i in range(1, len(encoded)):
            res[i] = encoded[i - 1] ^ res[i - 1]
        res.append(encoded[-1] ^ res[-1])
        return res
