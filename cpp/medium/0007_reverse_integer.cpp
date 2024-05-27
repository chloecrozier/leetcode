// Posted Solution: https://leetcode.com/problems/reverse-integer/solutions/5213698/simple-iterative-c-approach-beats-100-of-times/
// https://leetcode.com/problems/reverse-integer/description/
class Solution {
public:
    int reverse(int x) {
        long int res = 0;
        while(x != 0){
            res *= 10;
            res += x % 10;
            x = (x - (x % 10)) / 10;
        }
        if(res > INT_MAX || res < INT_MIN){
            return 0;
        }
        return res;
    }
};
