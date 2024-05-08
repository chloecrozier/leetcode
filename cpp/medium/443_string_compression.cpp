// https://leetcode.com/problems/string-compression/description/
class Solution {
public:
    int compress(vector<char>& chars) {
        int count = 1;
        char prev = chars[0];

        for(int i = 1; i < chars.size(); i++){
            if(prev == chars[i]){
                chars.erase(chars.begin() + i);
                count++;
                i--;
            } else{
                if(count > 1){
                    for(auto c : to_string(count)){
                        chars.insert(chars.begin() + i++, c);
                    }
                }
                prev = chars[i];
                count = 1;
            }
        }
        if(count > 1){
            for(auto c : to_string(count)){
                chars.insert(chars.end(), c);
            }
        }
        return chars.size();
    }
};
