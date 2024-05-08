// https://leetcode.com/problems/valid-palindrome/description/
class Solution {
public:
    bool isPalindrome(string s) {
        bool match = true;
        int i = 0;
        int j = s.length() - 1;
        while(match && i < j){
            char a = s[i];
            char b = s[j];
            if(!(isalnum(a)) || !(isalnum(b))){
                if(!(isalnum(a))){
                    i++;
                } else{
                    j--;
                }
            } else{
                if(tolower(a) != tolower(b)){
                    match = false;
                }
                i++;
                j--;
            }
        }
        return match;
    }
};
