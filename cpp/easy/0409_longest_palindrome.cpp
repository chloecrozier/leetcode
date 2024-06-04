// https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> letters;
        int count = 0;
        for(char c : s){
            letters[c]++;
            if(letters[c] == 2){
                letters[c] = 0;
                count += 2;
            }
        }
        for(const auto& pair : letters){
            if(pair.second == 1){
                return count + 1;
            }
        }
        return count;
    }
};
