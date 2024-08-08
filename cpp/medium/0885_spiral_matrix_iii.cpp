// https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08
class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        vector<vector<int>> visited;
        vector<int> space;
        space.push_back(rStart);
        space.push_back(cStart);
        visited.push_back(space);
        int direction = 0;
        int row = rStart;
        int col = cStart;
        int ringNum = 1;
        bool turning = false;

        while(visited.size() < (rows * cols)){
            vector<int> space;
            // east
            if(direction == 0){
                if(col < (cStart + ringNum)){
                    turning = false;
                    col++;
                } else{
                    direction++;
                    turning = true;
                }
            }
            // south
            if(direction == 1){
                if(row < (rStart + ringNum)){
                    turning = false;
                    row++;
                } else{
                    direction++;
                    turning = true;
                }
            }
            // west
            if(direction == 2){
                if(col > (cStart - ringNum)){
                    turning = false;
                    col--;
                } else{
                    direction++;
                    turning = true;
                }
            }
            // north
            if(direction == 3){
                if(row > (rStart - ringNum)){
                    turning = false;
                    row--;
                } else{
                    direction = 0;
                    ringNum++;
                    turning = true;
                }
            }
            if(row < rows && row >= 0 && col < cols && col >= 0 && !turning){
                space.push_back(row);
                space.push_back(col);
                visited.push_back(space);
            }
        }
        return visited;
    }
};
