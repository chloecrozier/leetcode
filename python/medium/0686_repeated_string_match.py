# https://leetcode.com/problems/repeated-string-match/
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(set(b)) > len(set(a)):
            return -1
        lenB = len(b)
        lenA = len(a)
        multiple = math.ceil((lenB / lenA)) + 1

        repeated = ""
        for i in range(multiple):
            repeated += a
        
        for i in range(len(repeated) - lenB):
            indexB = 0
            while indexB <= lenB:
                if indexB == lenB:
                    if len(repeated) - i - lenB >= lenA:
                        return multiple - 1
                    else:
                        return multiple
                else:
                    if repeated[i + indexB] != b[indexB]:
                        break
                indexB += 1

        return -1
