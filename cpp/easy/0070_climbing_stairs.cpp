// https://leetcode.com/problems/climbing-stairs/description/
class Solution {
public:
    int climbStairs(int n) {
        if(n <= 2){
            return n;
        }
        int permutations = 0;
        int lilStep = 1;
        int bigStep = 2;
        for(int i = 3; i <= n; i++){
            permutations = lilStep + bigStep;
            lilStep = bigStep;
            bigStep = permutations;
        }
        return permutations;
    }
};
