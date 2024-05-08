// https://leetcode.com/problems/length-of-last-word/description/
class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        int end = s.length() - 1;

        while(end >= 0 && s[end] == ' '){
            end--;
        }

        while(end >= 0 && s[end] != ' '){
            length++;
            end--;
        }

        return length;
    }
};
