# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return sum(arr)

        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        res = arr[-1]

        i = 0
        while i < len(arr):
            j = i + 2
            while j < len(arr):
                if i == 0:
                    res += arr[j]
                else:
                    res += arr[j] - arr[i - 1]
                j += 2
            i += 1
            
        return res
