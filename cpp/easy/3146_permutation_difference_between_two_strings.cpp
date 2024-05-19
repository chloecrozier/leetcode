// https://leetcode.com/problems/permutation-difference-between-two-strings/description/
class Solution {
public:
    int findPermutationDifference(string s, string t) {
        unordered_map<char, int> letters;
        int sum = 0;
        for(int i = 0; i < s.size(); i++){
            letters[s[i]] = i;
        }
        for(int i = 0; i < t.size(); i++){
            sum += abs(i - letters[t[i]]);
        }
        return sum;
    }
};
