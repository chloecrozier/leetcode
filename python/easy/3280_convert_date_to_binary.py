# https://leetcode.com/problems/convert-date-to-binary/description/
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ls = date.split("-")
        res = []
        for i in range(len(ls)):
            res.append(bin(int(ls[i]))[2:])
            res.append("-")
        return "".join(res[:-1])
