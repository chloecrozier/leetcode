// https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution {
public:
    string reverseWords(string s) {
        int i = -1;
        string w = "";
        bool word = false;
        
        while(++i < s.length()){
            if(s[i] == ' '){
                word = false;
            } else{
                w += s[i];
                word = true;
            }
            if(i == s.length() - 1){
                word = false;
            }
            if(w.length() > 0 && !word){
                w += " ";
                s.insert(0, w);
                s.erase(i + 1, w.length());
                w = "";
            }
        }
        while(s[--i] == ' '){
            s.pop_back();
        }

        return s;
    }
};
