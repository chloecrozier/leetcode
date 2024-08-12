// https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=daily-question&envId=2024-08-12
class KthLargest {
public:
    vector<int> list;
    int k = 0;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for(int i = 0; i < nums.size(); i++){
            list.push_back(nums[i]);
        }
        sort(list.begin(), list.end());
    }
    
    int add(int val) {
        for(int i = 0; i < list.size(); i++){
            if(val <= list[i]){
                list.insert(list.begin() + i, val);
                return list[list.size() - k];
            }
        }
        list.push_back(val);
        return list[list.size() - k];
    }
};
