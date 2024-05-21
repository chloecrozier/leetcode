// https://leetcode.com/problems/counting-bits/description/
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> v(n + 1, 0);
        int x, count;

        for(int i = 0; i <= n; i++){
            x = i;
            count = 0;
            while(x != 0){
                x = x & (x - 1);
                count++;
            }
            v[i] = count;
        }
        return v;
    }
};
