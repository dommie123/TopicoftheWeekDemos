import {BinarySearchTree} from "./binary-search-tree-js";

function main() {
    let bst = new BinarySearchTree();
    bst.insert(10);
    bst.insert(20);
    bst.insert(30);
    bst.insert(40);
    bst.insert(50);
    bst.insert(60);
    bst.insert(70);
    bst.insert(80);
    bst.insert(90);
    bst.insert(100);
    console.log("Inserted elements 10 through 100\n");

    console.log("In Order Traversal of BST before deletion: ")
    bst.inorder()

    console.log("\n Deleting element 40...")
    bst.delete(40)
    console.log("Deleting element 70...")
    bst.delete(70)
    console.log("Deleting element 10... \n")
    bst.delete(10)

    console.log("In Order Traversal of BST after deletion: ")
    bst.inorder()

    console.log(`\nPrinting element ${bst.search(100)}...`)
    console.log(`Printing element ${bst.search(20)}...`)
    console.log(`Printing element ${bst.search(50)}...`)
    console.log(`Trying to print element 40, but returns ${bst.search(40)}...`)
    console.log("\nEnd of demo! Exiting program...")
}

main()