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
    
    def array_to_tree(array):
        #This should just be quick sort
        """ 
        Find middle index of array (right middle index if array is even)
        Pop index and add to tree
        Go to righter most array
        Find middle index of the array (right middle index if array is even)
        Pop index and add to tree
        Go to righter most array

        If ther are no more righter most array, go to the array one to the left and find the middle index
        Pop index and add to tree
        Go to the righter most array
        Find middle index of the array (right middle index if array is even)
        Pop index and add to tree
        Go to righter most array

        Repeat steps until all elements are added to tree; tree will be even in height
        """
        return 0
        
# tree = TreeNode(8)
# tree.insert(16)
# tree.insert(4)
# tree.insert(15)
# tree.insert(17)
# tree.insert(5)
# tree.insert(3)

# tree.preorder_traversal()
# print()
# tree.delete_node(5)
# tree.preorder_traversal()

#Array Testing
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(len(array))
print(array)
new_array = array[(len(array)//2):]
print(new_array)
new_array.pop(0)
print()

array = new_array
print(array)
new_array = array[(len(array)//2):]
print(new_array)
new_array.pop(0)
print()

array = new_array
print(array)
new_array = array[(len(array)//2):]
print(new_array)
new_array.pop(0)
print()

print(new_array)