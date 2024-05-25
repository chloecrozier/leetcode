// https://leetcode.com/problems/reverse-prefix-of-word/description/
class Solution {
public:
    string reversePrefix(string word, char ch) {
        if(word.find(ch) == -1){
            return word;
        }

        string prefix = "";
        char curr = word[0];
        while(curr != ch && word.size() > 0){
            prefix = curr + prefix;
            word.erase(word.begin());
            curr = word[0];
        }
        word.erase(word.begin());
        return ch + prefix + word;
    }
};
