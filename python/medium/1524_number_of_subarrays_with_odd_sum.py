# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2025-02-25
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 0
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                even += 1
            else:
                odd, even = even + 1, odd
            count += odd

        return count % (pow(10, 9) + 7)
