// https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-08-07
class Solution {
public:
    string customSortString(string order, string s) {
        map<char, int> map;
        string res = "";
        for(char c : s){
            map[c]++;
        }
        for(char c : order){
            if(map.find(c) != map.end()){
                for(int i = 0; i < map[c ]; i++){
                    res += c;
                }
                map.erase(c);
            }
        }
        for(auto entry : map){
            for(int i = 0; i < entry.second; i++){
                cout << entry.second << endl;
                res += entry.first;
            }
        }
        return res;
    }
};
