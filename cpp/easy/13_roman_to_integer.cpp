// https://leetcode.com/problems/roman-to-integer/description/
class Solution {
public:
    int getVal(char c) {
        if(c == 'I') {
            return 1;
        } else if(c == 'V') {
            return 5;
        } else if(c == 'X') {
            return 10;
        } else if(c == 'L') {
            return 50;
        } else if(c == 'C') {
            return 100;
        } else if(c == 'D') {
            return 500;
        } else{
            return 1000;
        }
    }

    int romanToInt(string s) {
        int total = 0;
        for(int i = 0; i < s.length(); i++) {
            if(i + 1 < s.length()) {
                int num1 = getVal(s[i]);
                int num2 = getVal(s[i + 1]);
                if(num1 < num2) {
                    total = total - num1 + num2;
                    i++;
                } else {
                    total += num1;
                }
            } else{
                total += getVal(s[i]);
            }
        }
        return total;
    }
};
