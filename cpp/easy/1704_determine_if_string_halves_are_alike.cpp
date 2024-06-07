// https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-06-07
class Solution {
public:
    bool halvesAreAlike(string s) {
        int count = 0;
        for(int i = 0; i < s.length() / 2; i++){
            char left = tolower(s[i]);
            char right = tolower(s[i + s.length() / 2]);
            if(left == 'a' || left == 'e' || left == 'i' || left == 'o' || left == 'u'){
                count++;
            }
            if(right == 'a' || right == 'e' || right == 'i' || right == 'o' || right == 'u'){
                count--;
            }
        }
        return count == 0;
    }
};
