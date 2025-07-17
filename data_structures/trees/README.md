# README for Tree Data Structures

This directory contains information and examples related to tree data structures, which are a fundamental concept in computer science. Trees are used to represent hierarchical data and are essential for various algorithms and data manipulation techniques.

## Overview of Tree Data Structures

A tree is a data structure that consists of nodes connected by edges. Each tree has a root node, and every node can have zero or more child nodes. The main characteristics of trees include:

- **Root**: The top node of the tree.
- **Leaf**: A node that has no children.
- **Height**: The length of the longest path from the root to a leaf.
- **Depth**: The length of the path from the root to a specific node.

## Common Types of Trees

1. **Binary Tree**: Each node has at most two children.
2. **Binary Search Tree (BST)**: A binary tree where the left child contains values less than the parent node, and the right child contains values greater than the parent node.
3. **AVL Tree**: A self-balancing binary search tree.
4. **Red-Black Tree**: A balanced binary search tree with additional properties to ensure balance.
5. **N-ary Tree**: A tree where each node can have at most N children.

## Implementation Examples

Binary Tree
```cpp

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

TreeNode* insert(TreeNode* root, int val){
    if (!root) return new TreeNode(val); // base case, empty spot found
    if (val < root-> val) { //left smaller than node's value
        root->left = insert(root->left, val);
    }
    else{ //right >= node value
        root->right = insert(root->right, val);
    }
    return root;
}

void inorder(TreeNode* root){ //left -> node -> right
    if (!root) return;
    inorder(root->left);
    cout << root -> val << " ";
    inorder(root->right);
}

void preorder(TreeNode* root){ //node -> left -> right
    if (!root) return;
    cout << root -> val << " ";
    preorder(root->left);
    preorder(root->right);
}

void postorder(TreeNode* root){ //left -> right -> node
    if (!root) return;
    preorder(root->left);
    preorder(root->right);
    cout << root -> val << " ";
}

bool search(TreeNode* root, int val){
    if (!root) return false;
    if (root->val == val) return true;
    if (val < root->val) return search(root->left, val);
    else return search(root->right,val);
}

//need both of these to delete
TreeNode* findMin(TreeNode* node){
    while(node->left) node = node->left;
    return node;
}

TreeNode* deleteNode(TreeNode* root, int key){
    if (!root) return nullptr;
    if (key < root->val) {
        root->left = deleteNode(root->left, key);//go left
    }
    else if (key > root->val) {
        root->right = deleteNode(root->right, key); // Go right
    } 
    else {
        // Node found
        if (!root->left) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
        } else if (!root->right) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
        }

        // Case 3: Two children
        TreeNode* minNode = findMin(root->right);       // or max in left
        root->val = minNode->val;                       // Copy value
        root->right = deleteNode(root->right, minNode->val); // Delete duplicate
    }
    return root;
}

int height(TreeNode* root){
    if (!root) return 0;
    return 1 + max(height(root->left), height(root->right));
}

int size(TreeNode* root) {
    if (!root) return 0;
    return 1 + size(root->left) + size(root->right);
}

int findMinValue(TreeNode* root) {
    if (!root) throw runtime_error("Empty tree");
    while (root->left) root = root->left;
    return root->val;
}

int findMaxValue(TreeNode* root) {
    if (!root) throw runtime_error("Empty tree");
    while (root->right) root = root->right;
    return root->val;
}
```
## Examples and Problems

This section will include various examples and problems related to tree data structures, including:

- Traversal methods (In-order, Pre-order, Post-order)
- Finding the height of a tree
- Searching for a value in a tree
- Inserting and deleting nodes in a binary search tree
- Balancing trees

## Resources

- [GeeksforGeeks - Tree Data Structure](https://www.geeksforgeeks.org/data-structures/tree/)
- [LeetCode - Tree Problems](https://leetcode.com/tag/tree/)

Feel free to explore the examples and problems provided in this directory to enhance your understanding of tree data structures!

## LeetCode Problems

| Problem | Difficulty | Issues/Mistakes | Videos |
|---------|------------|-----------------|--------|
| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/) | Easy | | |
| [Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) | Easy | Recursion | |
| [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/) | Easy | | |
| [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/) | Medium | | |
| [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | | |
| [Subtree Of Another Tree](http://leetcode.com/problems/subtree-of-another-tree/description/) | Easy | | |

| [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/) | Easy | | |
| [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/) | Easy | | |
| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | | |
| [Lowest Common Ancestor Of A Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/) | Medium | | |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/) | Medium | | |
| [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | | |
| [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/) | Easy | | |
| [Kth Smallest Element In A Bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/) | Medium | | |