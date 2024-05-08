// https://leetcode.com/problems/keyboard-row/description/
class Solution {
public:
    bool inRow(unordered_set<char> set, string s){
        for(char c : s){
            if(set.count(tolower(c)) == 0){
                return false;
            }
        }
        return true;
    }

    vector<string> findWords(vector<string>& words) {
        vector<string> v;
        // string s1 = "qwertyuiop";
        // string s2 = "asdfghjkl";
        // string s3 = "asdfghjkl";
        unordered_set<char> s1 {'q','w','e','r','t','y','u','i','o','p'};
        unordered_set<char> s2 {'a','s','d','f','g','h','j','k','l'};
        unordered_set<char> s3 {'z','x','c','v','b','n','m'};

        for(auto word : words){
            if(inRow(s1, word) || inRow(s2, word) || inRow(s3, word)){
                v.push_back(word);
            }
        }
        return v;
    }
};
