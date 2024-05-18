// Posted Solution: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/solutions/5172788/simple-c-solution-beats-100-of-times/
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
class Solution {
public:
    int differenceOfSums(int n, int m){
        int res = 0;
        for(int i = 1; i <= n; i++){
            if((i / m) == (double(i) / double(m))){
                res -= i;
            } else{
                res += i;
            }
        }
        return res;
    }
};
