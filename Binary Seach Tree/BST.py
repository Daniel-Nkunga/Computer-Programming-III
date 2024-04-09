class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self): #Prints nodes in ascending order
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self): #Prints nodes in the order they appear
        print(self.value) 
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self): #Prints lowest node while still following pattern
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
        
    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete_node(self, value):
        if self is None:
            return self
        
        if value < self.value:
            self.left = self.left.delete_node(value)
        elif value > self.value:
            self.right = self.right.delete_node(value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp #Deletes node
            elif self.right is None:
                temp = self.left
                self = None
                return temp #Deletes node
            
            #For nodes with two children
            temp = self.get_min_value_node(self.right) #Shift tree from right children
            self.value = temp.value
            self.right = self.right.delete_node(temp.value)

        return self

    def in_order_successor(self, target):
        if self.value <= target:
            if self.right:
                return self.right.in_order_successor(target)
            else:
                return None  
        else:
            left_successor = None
            if self.left:
                left_successor = self.left.in_order_successor(target)
            return left_successor if left_successor else self

    
    @staticmethod
    def array_to_tree_helper(array, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(array[mid])
        
        root.left = TreeNode.array_to_tree_helper(array, start, mid - 1)
        root.right = TreeNode.array_to_tree_helper(array, mid + 1, end)
        
        return root

    @staticmethod
    def array_to_tree(array):
        if not array:
            return None
        
        return TreeNode.array_to_tree_helper(array, 0, len(array) - 1)

    def rotate_left(self):
        if not self.right:
            return  # Case where there is no right child to rotate
        
        # Save relevant values
        a = self.value
        b = self.right.value
        A = self.left
        B = self.right.left
        C = self.right.right

        # Reassign values and children
        self.value = b
        self.left = TreeNode(a)
        self.left.left = A
        self.left.right = B
        self.right = C

    def rotate_right(self):
        if not self.left:
            return  # Case where there is no left child to rotate
        
        # Save relevant values
        a = self.value
        b = self.left.value
        A = self.left.left
        B = self.left.right
        C = self.right

        # Reassign values and children
        self.value = b
        self.right = TreeNode(a)
        self.right.left = B
        self.right.right = C
        self.left = A

def main():
    #Examples
    print("Array to Tree")
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(array)
    tree = TreeNode.array_to_tree(array)
    tree.preorder_traversal()
    print()

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

if __name__ == "__main__":
    main()