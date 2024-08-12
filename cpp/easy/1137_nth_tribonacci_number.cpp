// https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=daily-question&envId=2024-08-10
class Solution {
public:
    int tribonacci(int n) {
        int list[38];
        list[0] = 0;
        list[1] = 1;
        list[2] = 1;
        for(int i = 0; i <= n - 3; i++){
            list[i + 3] = list[i] + list[i + 1] + list[i + 2];
        }
        return list[n];
    }
};≈
