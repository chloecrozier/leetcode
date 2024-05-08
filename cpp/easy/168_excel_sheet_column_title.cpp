// https://leetcode.com/problems/excel-sheet-column-title/description/
class Solution {
public:
    string convertToTitle(int num) {
        string col = "";
        while(num > 0){
            num--;
            col += num % 26 + 'A';
            num /= 26;
        }
        reverse(col.begin(), col.end());
        return col;
    }
};
