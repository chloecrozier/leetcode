// https://leetcode.com/problems/average-of-levels-in-binary-tree/submissions/1273835381/?envType=study-plan-v2&envId=top-interview-150
class Solution {
public:
    void getAves(TreeNode* root, vector<double>& res, vector<int>& count, int level){
        if(root != NULL){
            if(res.size() < level + 1){
                res.push_back(root->val);
                count.push_back(1);
            } else{
                res[level] += root->val;
                count[level]++;
            }
            getAves(root->left, res, count, level + 1);
            getAves(root->right, res, count, level + 1);
        }
    }

    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        vector<int> count;
        getAves(root, res, count, 0);
        for(int i = 0; i < res.size(); i++){
            res[i] /= count[i];
        }
        return res;
    }
};
