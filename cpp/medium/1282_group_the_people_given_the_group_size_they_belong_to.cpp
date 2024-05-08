// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        map<int, vector<int>> m;
        vector<vector<int>> v;
        int guest = 0;

        for(auto entry : groupSizes){
            m[entry].push_back(guest++);
            
            if(m[entry].size() == entry){
                v.push_back(m[entry]);
                m[entry].clear();
            }
        }
        return v;
    }
};
