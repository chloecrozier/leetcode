# https://leetcode.com/problems/sentence-similarity-iii/description/?envType=daily-question&envId=2024-10-06
class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        l1 = s1.split(' ')
        l2 = s2.split(' ')
        # ensure that l1 contains the same or more words than l2
        if len(l2) > len(l1):
            temp = l1
            l1 = l2
            l2 = temp

        start = 0
        while l1[start : start + 1] == l2[start : start + 1]:
            start += 1
        end = start + 1

        while end <= len(l1):
            if l1[0 : start] + l1[end : len(l1)] == l2:
                return True
            else:
                end += 1
                
        return False
