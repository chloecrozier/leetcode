// Posted Solution: https://leetcode.com/problems/score-of-a-string/solutions/5161665/simple-iterative-c-approach-beats-100-of-times/
// https://leetcode.com/problems/score-of-a-string/description/
class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        for(int i = 0; i < s.length() - 1; i++){
            score += abs(s[i] - s[i + 1]);
        }
        return score;
    }
};
