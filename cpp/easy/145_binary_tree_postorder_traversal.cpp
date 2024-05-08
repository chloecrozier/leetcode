// https://leetcode.com/problems/binary-tree-postorder-traversal/description/
class Solution {
public:
    void addVal(TreeNode* root, vector<int>& v){
        if(root != NULL){
            addVal(root->left, v);
            addVal(root->right, v);
            v.push_back(root->val);
        }
    }

    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> v;
        addVal(root, v);
        return v;
    }
};
