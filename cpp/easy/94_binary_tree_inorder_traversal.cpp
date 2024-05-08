// https://leetcode.com/problems/binary-tree-inorder-traversal/description/
class Solution {
public:

    void addVals(TreeNode* root, vector<int>& v){
        if(root != NULL){
            addVals(root->left, v);
            v.push_back(root->val);
            addVals(root->right, v);
        }
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> v;
        addVals(root, v);
        return v;
    }
};
