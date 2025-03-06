# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        res = []
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in freq:
                freq[sortedS].append(s)
            else:
                freq[sortedS] = [s]

        for key, value in freq.items():
            res.append(value)

        return res
