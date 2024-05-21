// https://leetcode.com/problems/ransom-note/description/
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<int, int> m;
        for(int i = 0; i < magazine.length(); i++){
            m[magazine[i] - 'a']++;
        }
        for(int i = 0; i < ransomNote.length(); i++){
            if(m[ransomNote[i] - 'a'] == 0){
                return false;
            }
            m[ransomNote[i] - 'a']--;
        }
        return true;
    }
};
