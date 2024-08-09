// https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09
class Solution {
public:
    bool rowSum(vector<vector<int>>& grid, int r, int c){
        int col1 = grid[r - 1][c - 1] + grid[r - 1][c] + grid[r - 1][c + 1];
        int col2 = grid[r][c - 1] + grid[r][c] + grid[r][c + 1];
        int col3 = grid[r + 1][c - 1] + grid[r + 1][c] + grid[r + 1][c + 1];
        return (col1 == col2) && (col1 == col3);
    }

    bool colSum(vector<vector<int>>& grid, int r, int c){
        int row1 = grid[r - 1][c - 1] + grid[r][c - 1] + grid[r + 1][c - 1];
        int row2 = grid[r - 1][c] + grid[r][c] + grid[r + 1][c];
        int row3 = grid[r - 1][c + 1] + grid[r][c + 1] + grid[r + 1][c + 1];
        return (row1 == row2) && (row1 == row3);
    }

    bool diagSum(vector<vector<int>>& grid, int r, int c){
        int leftDownDiag = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1];
        int leftUpDiag = grid[r + 1][c - 1] + grid[r][c] + grid[r - 1][c + 1];
        return leftDownDiag == leftUpDiag;
    }

    bool distinctNums(vector<vector<int>>& grid, int r, int c){
        unordered_set<int> nums;
        for(int i = r - 1; i <= r + 1; i++){
            for(int j = c - 1; j <= c + 1; j++){
                if(grid[i][j] > 0 && grid[i][j] < 10){
                    nums.insert(grid[i][j]);
                }
            }
        }
        return nums.size() == 9;
    }

    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int numSquares = 0;
        if(grid[0].size() < 3 || grid.size() < 3){
            return numSquares;
        }
        for(int centerR = 1; centerR < grid.size() - 1; centerR++){
            for(int centerC = 1; centerC < grid[0].size() - 1; centerC++){
                bool rSum = rowSum(grid, centerR, centerC);
                bool cSum = colSum(grid, centerR, centerC);
                bool dSum = diagSum(grid, centerR, centerC);
                bool distinct = distinctNums(grid, centerR, centerC);
                if(cSum && rSum && dSum && distinct){
                    numSquares++;
                }
            }
        }
        return numSquares;
    }
};
