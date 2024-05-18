// https://leetcode.com/problems/smallest-even-multiple/description/
class Solution {
public:
    int smallestEvenMultiple(int n) {
        return n % 2 == 0 ? n : 2 * n;
    }
};
