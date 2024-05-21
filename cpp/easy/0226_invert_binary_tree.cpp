// https://leetcode.com/problems/invert-binary-tree/description/
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root){
            TreeNode* temp = root->left;
            root->left = invertTree(root->right);
            root->right = invertTree(temp);
        }
        return root;
    }
};
