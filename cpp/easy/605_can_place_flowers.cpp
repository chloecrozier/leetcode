// https://leetcode.com/problems/can-place-flowers/
class Solution {
public:
    bool canPlaceFlowers(vector<int>& f, int n) {
        f.insert(f.begin(), 0);
        f.push_back(0);

        int count;
        for(int i = 1; i < f.size() - 1; i++){
            if(f[i - 1] + f[i] + f[i + 1] == 0){
                n--;
                i++;
            }
        }
        return n <= 0;
    }
};
