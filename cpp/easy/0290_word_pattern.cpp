// https://leetcode.com/problems/word-pattern/description/?source=submission-noac
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> patternMap;
        unordered_map<string, int> seen;
        vector<string> words;
        string word = "";
        for(int i = 0; i < s.length(); i++){
            if(s[i] != ' '){
                word += s[i];
            } else{
                words.push_back(word);
                word = "";
            }
        }
        words.push_back(word);

        if(pattern.length() != words.size()){
            return false;
        }

        patternMap[pattern[0]] = words[0];
        seen[words[0]]++;
        for(int i = 1; i < pattern.length(); i++){
            if(patternMap.count(pattern[i]) > 0){
                if(patternMap[pattern[i]] != words[i]){
                    return false;
                }
            } else{
                if(seen[words[i]] != 0){
                    return false;
                }
                patternMap[pattern[i]] = words[i];
                seen[words[i]]++;
            }
        }
        return true;
    }
};
