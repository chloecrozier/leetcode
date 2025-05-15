# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/?envType=daily-question&envId=2025-05-13
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res = []
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        for transformation in range(t):
            temp = [0] * 26
            for i in range(len(freq)):
                if freq[i] > 0:
                    if i == 25:
                        temp[0] += freq[i]
                        temp[1] += freq[i]
                    else:
                        temp[i + 1] += freq[i]
            freq = temp
        return sum(freq) % (pow(10, 9) + 7)
