// https://leetcode.com/problems/valid-anagram/submissions/1258401000/
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        unordered_map<char, int> letters;
        for(auto letter : s){
            letters[letter]++;
        }
        for(auto letter : t){
            letters[letter]--;
        }
        for(auto &entry : letters){
            if(entry.second != 0){
                return false;
            }
        }
        return true;
    }
};
