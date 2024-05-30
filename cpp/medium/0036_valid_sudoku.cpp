// https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> box[9];
        for(int r = 0; r < board.size(); r++){
            for(int c = 0; c < board.size(); c++){
                char num = board[r][c];
                if(num != '.'){
                    if(rows[r].count(num) || cols[c].count(num) || box[((r / 3) * 3) + (c / 3)].count(num)){
                        return false;
                    } else{
                        rows[r].insert(num);
                        cols[c].insert(num);
                        box[((r / 3) * 3) + (c / 3)].insert(num);
                    }
                }
            }
        }
        return true;
    }
};
