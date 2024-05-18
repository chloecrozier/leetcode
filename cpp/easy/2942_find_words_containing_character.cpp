// https://leetcode.com/problems/find-words-containing-character/description/
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> res;
        for(int i = 0; i < words.size(); i++){
            for(auto letter : words[i]){
                if(letter == x){
                    res.push_back(i);
                    break;
                }
            }
        }
        return res;
    }
};
