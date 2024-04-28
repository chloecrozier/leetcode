// https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution {
public:
    int maxOperations(vector<int>& n, int k) {
        map<int, int> m;
        int count = 0, x = 0;
        
        for(int i = 0; i < n.size(); i++){
            x = k - n[i];
            if(m[x] > 0){
                m[x]--;
                count++;
            } else{
                m[n[i]]++;
            }
        }
        return count;
    }
};
