// https://leetcode.com/problems/jewels-and-stones/description/
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_map<char, int> letters;
        int sum = 0;

        for(auto c : stones){
            letters[c]++;
        }
        for(auto c : jewels){
            sum += letters[c];
        }
        return sum;
    }
};
