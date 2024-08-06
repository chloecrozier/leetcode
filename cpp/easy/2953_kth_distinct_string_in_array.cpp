// https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=daily-question&envId=2024-08-05
class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        map<string, int> words;
        for(auto word: arr){
            words[word]++;
        }
        int count = 0;
        for(auto key : arr){
            if(words[key] == 1){
                count++;
            }
            if(count == k){
                return key;
            }
        }
        return "";
    }
};
