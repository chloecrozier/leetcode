// https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> tri = {{1}};

        for(int i = 1; i <= rowIndex; i++){
            vector<int> row = {1};
            for(int j = 1; j <= i; j++){
                if(j == i){
                    row.push_back(1);
                } else{
                    row.push_back(tri[i - 1][j - 1] + tri[i - 1][j]);
                }
            }
            tri.push_back(row);
        }
        
        return tri[rowIndex];
    }
};
