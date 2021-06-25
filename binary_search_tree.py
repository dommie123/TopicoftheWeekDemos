# Actual BST implementation
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Calls the recursion function that searches the tree for a node.
    def search(self, key):
        return self.search_rec(self.root, key)

    # Searches the tree for a specific key in a recursive manner.
    # If found, returns the node that has the key. Otherwise, returns
    # null.
    def search_rec(self, root, key):
        # If the key cannot be found, return null.
        if root is None:
            return None

        # If the key is found, return the node. Otherwise, recurse down the tree.
        if root.key == key:
            return root
        elif key < root.key:
            return self.search_rec(root.left, key)
        elif key > root.key:
            return self.search_rec(root.right, key)

    # Calls the recursion function that inserts a node into the BST.
    def insert(self, key):
        self.root = self.insert_rec(self.root, key)
    
    # Recursive function to insert a new key into BST.
    def insert_rec(self, root, key):
        # If node is empty, insert key in this node and return it.
        if root == None:
            root = Node(key)
            return root

        # Otherwise, recurse down the tree.
        if key < root.key:
            root.left = Node(key) if root.left is None else self.insert_rec(root.left, key)
        elif key > root.key:
            root.right = Node(key) if root.right is None else self.insert_rec(root.right, key)

        return root

    # Calls the recursion function for removing a key from the BST.
    def delete(self, key):
        return self.delete_rec(self.root, key)

    # Searches the BST for the key to remove, then removes the key.
    def delete_rec(self, root, key):
        # Base case: if tree is empty
        if root == None:
            return root

        # Otherwise, recurse down the tree.
        if key < root.key:
            root.left = self.delete_rec(root.left, key)
        elif key > root.key:
            root.right = self.delete_rec(root.right, key)

        # If key is equal to the root key, delete this node.
        else:
            # node with one or no children.
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # node with two children: Get the inorder successor
            root.key = self.min_value(root.right)

            # Delete the inorder successor
            root.right = self.delete_rec(root.right, root.key)

        return root

    # Calls the recursive method for inorder traversal of the BST.
    def inorder(self):
        self.inorder_rec(self.root)
    
    # Recursively traverses the BST inorder.
    def inorder_rec(self, root):
        if root:
            self.inorder_rec(root.left)
            print(root.key)
            self.inorder_rec(root.right)
    
    def min_value(self, root):
        minv = root.key
        while root.left:
            minv = root.left.key
            root = root.left
        return minv

# Class containing the item as well as the left and right nodes.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"Node {self.key} Left: {self.left} Right: {self.right}\n"