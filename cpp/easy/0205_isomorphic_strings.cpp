// https://leetcode.com/problems/isomorphic-strings/description/
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, int> sMap;
        map<char, int> tMap;

        if(s.length() != t.length()){
            return false;
        }

        for(int i = 0; i < s.length(); i++){
            if(sMap[s[i]] != tMap[t[i]]){
                return false;
            }

            sMap[s[i]] = i + 1;
            tMap[t[i]] = i + 1;
        }
        return true;
    }
};
