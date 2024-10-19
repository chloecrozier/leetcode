# https://leetcode.com/problems/integer-to-english-words/description/
class Solution:
    def ones(self, num: int) -> str:
        if num == 1:
            return "One"
        elif num == 2:
            return "Two"
        elif num == 3:
            return "Three"
        elif num == 4:
            return "Four"
        elif num == 5:
            return "Five"
        elif num == 6:
            return "Six"
        elif num == 7:
            return "Seven"
        elif num == 8:
            return "Eight"
        elif num == 9:
            return "Nine"
        else:
            return ""
    
    def teens(self, num: int) -> str:
        if num == 10:
            return "Ten"
        elif num == 11:
            return "Eleven"
        elif num == 12:
            return "Twelve"
        elif num == 13:
            return "Thirteen"
        elif num == 15:
            return "Fifteen"
        elif num == 18:
            return "Eighteen"
        else:
            return self.ones(num % 10) + "teen"

    def tens(self, num: int) -> str:
        onesDigits = self.ones(num % 10)
        if onesDigits != "":
            onesDigits = " " + onesDigits

        if num // 10 == 2:
            return "Twenty" + onesDigits
        elif num // 10 == 3:
            return "Thirty" + onesDigits
        elif num // 10 == 4:
            return "Forty" + onesDigits
        elif num // 10 == 5:
            return "Fifty" + onesDigits
        elif num // 10 == 6:
            return "Sixty" + onesDigits
        elif num // 10 == 7:
            return "Seventy" + onesDigits
        elif num // 10 == 8:
            return "Eighty" + onesDigits
        else:
            return "Ninety" + onesDigits

    def getChunk(self, s: str) -> str:
        onesDigits = self.ones(int(s[2]) % 10)
        if onesDigits != "":
            onesDigits = " " + onesDigits

        if s[0:2] == '00': # 000 001 007... etc
            return self.ones(int(s[-1])) # can return "zero"
        elif s[0] == '0': # 010 050 099
            if s[1] == '1':
                return self.teens(int(s[1:3]))
            else:
                return self.tens(int(s[1:3]))
        else: # 101 789 800 999
            if s[1:2] == '00': # 100 500 900
                return self.ones(int(s[0])) + " Hundred"
            elif s[1] == '0': # 101 707
                return self.ones(int(s[0])) + " Hundred" + onesDigits
            else: # 123 456 789
                if s[1] == '1':
                    return self.ones(int(s[0])) + " Hundred " + self.teens(int(s[1:3]))
                else:    
                    return self.ones(int(s[0])) + " Hundred " + self.tens(int(s[1:3]))
                    
    def getPlace(self, place: int) -> str:
        if place <= 1:
            return ""
        elif place == 2:
            return " Thousand"
        elif place == 3:
            return " Million"
        else:
            return " Billion"


    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        res = ''
        s = str(num)
        chunks = (len(s) // 3)# len=10 -> (10 // 3) + 1 = 3 + 1 = 4
        start = len(s) % 3 # len=10 -> 10 % 3 = 1
        placeIndex = chunks
        if start:
            placeIndex += 1

        if start == 1:
            res += self.ones(int(s[0])) + self.getPlace(placeIndex)
            placeIndex -= 1
        elif start == 2:
            if s[0] == '1':
                res += self.teens(int(s[0:2])) + self.getPlace(placeIndex)
            else:
                res += self.tens(int(s[0:2])) + self.getPlace(placeIndex)
            placeIndex -= 1

        for i in range(start, len(s), 3):
            hundreds = self.getChunk(s[i:i+3])
            if hundreds != '':
                if res:
                    res += ' '
                res += self.getChunk(s[i:i+3]) + self.getPlace(placeIndex)
            placeIndex -= 1
        return res
