// https://leetcode.com/problems/path-sum/description/
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root == NULL){
            return false;
        }
        if(root->left == NULL && root->right == NULL){
            if(targetSum - root->val == 0){
                return true; 
            }
        }

        bool l = hasPathSum(root->left, targetSum - root->val);
        bool r = hasPathSum(root->right, targetSum - root->val);
    
        return l || r;
    }
};
