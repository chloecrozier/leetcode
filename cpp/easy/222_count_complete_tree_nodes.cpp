// https://leetcode.com/problems/count-complete-tree-nodes/description/
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(root){
            return 1 + countNodes(root->left) + countNodes(root->right);
        }
        return 0;
    }
};
