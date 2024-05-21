// https://leetcode.com/problems/balanced-binary-tree/description/
class Solution {
public:
    int getDepth(TreeNode* root){
        if(root == NULL){
            return 0;
        }
        int l = getDepth(root->left);
        int r = getDepth(root->right);

        if((abs(l - r) > 1) || l == -1 || r == -1){
            return -1;
        } else{
            return max(l, r) + 1;
        }  
    }

    bool isBalanced(TreeNode* root) {
        if(root == NULL || getDepth(root) != -1){
            return true;
        }
        return false;
    }
};
