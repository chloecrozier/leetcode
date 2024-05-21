// https://leetcode.com/problems/search-in-a-binary-search-tree/description/
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root == NULL){
            return root;
        }
        if(root->val > val){
            return searchBST(root->left, val);
        } else if(root->val < val){
            return searchBST(root->right, val);
        } else{
            return root;
        }
    }
};
