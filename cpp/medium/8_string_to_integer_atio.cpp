// https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution {
public:
    int myAtoi(string s) {
        bool isNeg = false;
        bool isNum = false;
        long long int num = 0;
        int i = 0;
        while (i < s.length()) {
            if (!isNum) {
                if (s[i] == ' ') {
                    i++;
                } else if (s[i] == '0') {
                    i++;
                    isNum = true;
                } else if (s[i] == '-' || s[i] == '+') {
                    if(s[i] == '-'){
                        isNeg = true;
                    }
                    isNum = true;
                    i++;
                } else if (!isdigit(s[i])) {
                    break;
                } else {
                    isNum = true;
                    num = num * 10 + s[i] - '0';
                    if (num > INT_MAX) {
                        return isNeg ? INT_MIN : INT_MAX;
                    }
                    i++;
                }
            } else {
                if (!isdigit(s[i])) {
                    break;
                } else {
                    num = num * 10 + s[i] - '0';
                    if (num > INT_MAX) {
                        return isNeg ? INT_MIN : INT_MAX;
                    }
                    i++;
                }
            }
        }
        return isNeg ? -num : num;
    }
};
