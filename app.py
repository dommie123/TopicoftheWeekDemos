from binary_search_tree import BinarySearchTree

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(40)
    bst.insert(30)
    bst.insert(60)
    bst.insert(70)
    bst.insert(20)
    bst.insert(80)
    bst.insert(90)
    bst.insert(10)
    bst.insert(100)
    print("Inserted elements 10 through 100\n")

    print("Inorder traversal of BST before deletion:")
    bst.inorder()

    print("\nDeleting element 40...")
    bst.delete(40)
    print("Deleting element 70...")
    bst.delete(70)
    print("Deleting element 10...\n")
    bst.delete(10)

    print("Inorder traversal of BST after deletion:")
    bst.inorder()
    
    print(f"\nPrinting element 100... {bst.search(100)}")
    print(f"Printing element 20... {bst.search(20)}")
    print(f"Printing element 50... \n{bst.search(50)}")
    print(f"Trying to print element 40, but returns {bst.search(40)}")
    print(f"\nEnd of demo! Exiting program...")
