// https://leetcode.com/problems/merge-strings-alternately/
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i = 0, j = 0;
        string res = "";
        bool turn = true;
        while(i < word1.length() && j < word2.length()){
            if(turn){
                res += word1[i];
                i++;
                turn = false;
            } else{
                res += word2[j];
                j++;
                turn = true;
            }
        }
        if(i < word1.length()){
            res += word1.substr(i, word1.length());
        }
        if(j < word2.length()){
            res += word2.substr(j, word2.length());
        }
        return res;
    }
};
