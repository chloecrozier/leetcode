// https://leetcode.com/problems/longest-common-prefix/description/
class Solution {
public:
    string findCommonStart(string s1, string s2){
        int i = 0;
        string word = "";
        while(i <= s1.length() && i <= s2.length()){
            if(s1.substr(0, i) == s2.substr(0, i)){
                word = s1.substr(0, i);
            }
            i++;
        }
        return word;
    }

    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 1)
        {
            return strs[0];
        }

        string output = strs[0];
        for(auto &word : strs){
            output = findCommonStart(output, word);
        }

        return output;
    }
};
