// Posted Solution: https://leetcode.com/problems/power-of-two/solutions/5159421/simple-c-recursive-approach-beats-100-of-times/
// https://leetcode.com/problems/power-of-two/submissions/1258405244/
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n == 1){
            return true;
        }
        if(n == 0 || n % 2 != 0){
            return false;
        }
        return isPowerOfTwo(n / 2);
    }
};
