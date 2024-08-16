// https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution {
public:
    void recurse(string digits, int i, unordered_map <char, string> &keys, string combo, vector<string> &res){
        if(combo.length() == digits.size()){
            res.push_back(combo);
        }
        for(auto letter : keys[digits[i]]){
            combo += letter;
            recurse(digits, i + 1, keys, combo, res);
            combo = combo.substr(0, combo.length() - 1);
        }
    }

    vector<string> letterCombinations(string digits) {
        if(digits.empty()){
            return {};
        }
        unordered_map <char, string> keys = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        vector<string> res;
        string combo = "";
        recurse(digits, 0, keys, combo, res);
        return res;
    }
};
