// https://leetcode.com/problems/excel-sheet-column-number/description/
class Solution {
public:
    int titleToNumber(string s) {
        long int multiple = 1;
        long int total = 0;
        for(int i = s.size() - 1; i >= 0; i--){
            total += multiple * (s[i] % 64);
            multiple *= 26;
        }
        return total;
    }
};
