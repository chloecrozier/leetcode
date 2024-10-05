# https://leetcode.com/problems/permutation-in-string/description/?envType=daily-question&envId=2024-10-05
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        substrLen = len(s1)
        substrElems = {}
        for c in s1:
            if c in substrElems:
                substrElems[c] += 1
            else:
                substrElems[c] = 1
        
        for i in range(len(s2) - substrLen + 1):
            strElems = {}
            chunk = s2[i:i+substrLen] # get a subset of s2 of size s1
            for j in range(len(chunk)):
                if chunk[j] in substrElems:
                    if chunk[j] in strElems:
                        strElems[chunk[j]] += 1
                    else:
                        strElems[chunk[j]] = 1
                    if strElems[chunk[j]] > substrElems[chunk[j]]:
                        break
                    if substrElems == strElems:
                        return True
                else:
                    i = j
        return False
