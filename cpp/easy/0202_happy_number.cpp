// https://leetcode.com/problems/happy-number/description/
class Solution {
public:

    int getSum(int n){
        int total = 0;
        while(n != 0){
            total += pow(n % 10, 2);
            n /= 10;
        }
        return total;
    }

    bool isHappy(int n) {
        map<int, int> m;
        while(n != 1 && m.count(n) == 0){
            m[n]++;
            n = getSum(n);
        }
        return n == 1;
    }
};
