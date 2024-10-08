# https://leetcode.com/problems/encode-and-decode-strings/description/
class Solution:
    def encode(self, strs: List[str]) -> str:
        shift = 13
        res = ''
        for s in strs:
            for c in s:
                if c.isalpha():
                    if c.isupper():
                        res += chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
                    else:
                        res += chr(((ord(c) - ord('a') + shift) % 26) + ord('a'))
                else:
                    res += c
            res += '\0'

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        shift = 13
        res = []
        curr = ''
        for c in s:
            if c == '\0':
                res.append(curr)
                curr = ''
            else:
                if c.isalpha():
                    if c.isupper():
                        curr += chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
                    else:
                        curr += chr(((ord(c) - ord('a') - shift) % 26) + ord('a'))
                else:
                    curr += c
        return res
