// https://leetcode.com/problems/reverse-vowels-of-a-string/description/
class Solution {
public:
    string reverseVowels(string s) {
        int i = 0, j = s.length() - 1;
        while(i < j){
            i = s.find_first_of("aeiouAEIOU", i);
            j = s.find_last_of("aeiouAEIOU", j);
            if(i < j){
                swap(s[i++], s[j--]);
            }
        }
        return s;

        // vector<char> vowels;
        // char tmp;
        // for(auto c : s){
        //     tmp = tolower(c);
        //     if(tmp == 'a' || tmp == 'e' || tmp == 'i' || tmp == 'o' || tmp == 'u'){
        //         vowels.push_back(c);
        //     }
        // }

        // int lastVowel = vowels.size() - 1;
        // for(int i = 0; i < s.length(); i++){
        //     tmp = tolower(s[i]);
        //     if(tmp == 'a' || tmp == 'e' || tmp == 'i' || tmp == 'o' || tmp == 'u'){
        //         s[i] = vowels[lastVowel];
        //         lastVowel--;
        //     }
        // }
        // return s;
    }
};
