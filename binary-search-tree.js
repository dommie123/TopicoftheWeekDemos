// Actual BST implementation
class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    // Calls the recursion function that searches the tree for a node.
    search(key) {
        return this.searchRec(this.root, key);
    }

    // Searches the tree for a specific key in a recursive manner.
    // If found, returns the node that has the key. Otherwise, returns
    // null.
    searchRec(root, key) {
        // If the key cannot be found, return null.
        if (!root) {
            return null;
        }
        
        // If the key is found, return the node. Otherwise, recurse down the tree.
        if (root.key === key) {
            return root;
        } else if (root.key < key) {
            return this.searchRec(root.left, key);
        } else if (root.key > key) {
            return this.searchRec(root.right, key);
        }
    }
    
    // Calls the recursion function that inserts a node into the BST.
    insert(key) {
        this.root = this.insertRec(root, key);
    }

    // Recursive function to insert a new key into BST.
    insertRec(root, key) {
        // If node is empty, return the node.
        if (!root) {
            root = Node(key);
            return root;
        }
        
        // Otherwise, recurse down the tree.
        if (key < root.key) {
            root.left = this.insertRec(root.left, key);
        } else if (key > root.key) {
            root.right = this.insertRec(root.right, key);
        }
    }

    // Calls the recursion function for removing a key from the BST.
    delete(key) {

    }

    // Searches the BST for the key to remove, then removes the key.
    deleteRec(root, key) {

    }

    // Calls the recursive method for inorder traversal of the BST.
    inorder() {
        this.inorderRec(this.root);
    }

    // Recursively traverses the BST inorder.
    inorderRec(root) {
        if (root) {
            this.inorderRec(root.left);
            console.log(root.key);
            this.inorderRec(root.right);
        }
    }
}

// Class containing the item as well as the left and right nodes.
class Node {
    constructor(item) {
        this.key = item;
        this.left = this.right = null;
    }
}