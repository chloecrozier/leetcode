// https://leetcode.com/problems/binary-tree-preorder-traversal/description/
class Solution {
public:
    void addVal(TreeNode* root, vector<int>& v){
        if(root != NULL){
            v.push_back(root->val);
            addVal(root->left, v);
            addVal(root->right, v);
        }
    }

    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> v;
        addVal(root, v);
        return v;
    }
};
