// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
class Solution {
public:
    TreeNode* addNode(vector<int>& v, int start, int end){
        if(start > end){
            return NULL;
        }
        int mid = (end + start) / 2;
        TreeNode* node = new TreeNode(v[mid]);
        node->left = addNode(v, start, mid - 1);
        node->right = addNode(v, mid + 1, end);
        return node;
    }

    TreeNode* sortedArrayToBST(vector<int>& v) {
        if(v.size() == 0){
            return NULL;
        } else{
            return addNode(v, 0, v.size() - 1);
        }
    }
};
