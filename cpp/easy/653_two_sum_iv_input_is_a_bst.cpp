// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
class Solution {
public:
    bool searchSet(TreeNode* root, int k, unordered_set<int>& s) {
        if(root == NULL){
            return false;
        }
        if(s.count(k - root->val)){
            return true;
        }
        s.insert(root->val);
        return searchSet(root->left, k, s) || searchSet(root->right, k, s);
    }

    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> s;
        return searchSet(root, k, s);
    }
};
