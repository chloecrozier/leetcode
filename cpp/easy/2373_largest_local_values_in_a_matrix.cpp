// https://leetcode.com/problems/largest-local-values-in-a-matrix/description/?envType=daily-question&envId=2024-05-12
class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        vector<vector<int>> res;
        int r1, r2, r3;
        for(int i = 1; i < grid.size() - 1; i++){
            vector<int> subMax;
            for(int j = 1; j < grid.size() - 1; j++){
                r1 = max(max(grid[i-1][j-1], grid[i-1][j]), max(grid[i-1][j], grid[i-1][j+1]));
                r2 = max(max(grid[i][j-1], grid[i][j]), max(grid[i][j], grid[i][j+1]));
                r3 = max(max(grid[i+1][j-1], grid[i+1][j]), max(grid[i+1][j], grid[i+1][j+1]));
                subMax.push_back(max(max(r1, r2), max(r2, r3)));  
            }
            res.push_back(subMax);   
        }
        return res;
    }
};
