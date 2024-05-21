// https://leetcode.com/problems/pascals-triangle/description/
class Solution {
public:
    vector<int> getNextRow(vector<int> prev){
        vector<int> row;
        row.push_back(1);
        for(int i = 0; i < prev.size() - 1; i++){
            row.push_back(prev[i] + prev[i + 1]);
        }
        row.push_back(1);

        return row;
    }

    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> tri;
        tri.push_back({1});
        for(int i = 0; i < numRows - 1; i++){
            tri.push_back(getNextRow(tri[i]));
        }
        return tri;
    }
};
