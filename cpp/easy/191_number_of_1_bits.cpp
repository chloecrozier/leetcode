// https://leetcode.com/problems/number-of-1-bits/description/
class Solution {
public:
    int hammingWeight(uint32_t n) {
        long int count = 0;
        while(n != 0){
            n &= (n - 1);
            count++;
        }
        return count;
    }
};
