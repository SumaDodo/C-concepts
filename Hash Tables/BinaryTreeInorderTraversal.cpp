/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> nodeStack;
        vector<int> inorderVec;
        
        if (root == nullptr)
            return {};
            
        TreeNode* curNode = root;
        while(curNode!= nullptr || !nodeStack.empty()){
            while (curNode!= nullptr){
                nodeStack.push(curNode);
                curNode = curNode->left;
            }
            curNode = nodeStack.top();
            nodeStack.pop();
            inorderVec.push_back(curNode->val);
            curNode = curNode->right;
        }
        return inorderVec;
    }
};
