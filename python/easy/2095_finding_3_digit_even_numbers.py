# https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12
class Solution:
    def findEvenNumbers(self, a: List[int]) -> List[int]:
        res = []
        m = {}

        for i in range(len(a)):
            if a[i] in m:
                m[a[i]] += 1
            else:
                m[a[i]] = 1

        for i in range(100, 999, 2):
            # print(i // 100, i // 10 % 10, i % 10)
            if i // 100 not in m:
                i += 100
            else:
                if i // 10 % 10 not in m:
                    i += 10
                else:
                    if i // 100 == i // 10 % 10:
                        if m[i // 10 % 10] >= 2:
                            if i % 10 in m: 
                                if i % 10 == i // 100:
                                    if m[i % 10] >= 3:
                                        res.append(i)
                                else:
                                        res.append(i)
                    else:
                        if i % 10 in m: 
                            if i % 10 == i // 100 or i % 10 == i // 10 % 10:
                                if m[i % 10] >= 2:
                                    res.append(i)
                            else:
                                    res.append(i)
        return res
