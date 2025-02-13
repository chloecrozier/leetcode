# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        singleBit = True
        while i < len(bits):
            if bits[i] == 1:
                i += 1
                singleBit = False
            else:
                singleBit = True
            i += 1

        return singleBit
