#This is just a copy paste of my old main function

def main():
    #Examples
    print("Array to Tree")
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(array)
    tree = TreeNode.array_to_tree(array)
    tree.rotate_right()
    tree.preorder_traversal()
    print()

    print(tree.right.get_height())
    print(tree.height_factor())

    #Display 
    print("Print Inorder Traversal")
    tree.inorder_traversal()
    print()

    print("Print Preorder Traversal")
    tree.preorder_traversal()
    print()

    print("Print Postorder Traversal")
    tree.postorder_traversal()
    print()

    #Rotation Functions
    print("Rotate Left")
    tree.rotate_left()
    tree.preorder_traversal()
    print("Resetting Tree")
    tree = TreeNode.array_to_tree(array)
    print()

    print("Rotate Right")
    tree.rotate_right()
    tree.preorder_traversal()
    print("Resetting Tree")
    tree = TreeNode.array_to_tree(array)
    print()

    #Delete showcase
    print("Delete")
    print("Deleting 5")
    tree.delete_node(5)
    tree.preorder_traversal()
    print()

    #Successor Showcase
    print("Next Successor")
    print("Finding successor to 10")
    print(tree.in_order_successor(10).value)
    print()

    print("Done!")