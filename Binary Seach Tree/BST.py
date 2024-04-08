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

    # def array_to_tree(array):
    #     #This should just be quick sort
    #     """ 
    #     Find middle index of array (right middle index if array is even)
    #     Pop index and add to tree
    #     Go to righter most array

    #     Find middle index of the array (right middle index if array is even)
    #     Pop index and add to tree
    #     Go to righter most array

    #     If ther are no more righter most array, go to the array one to the left and find the middle index
    #     Pop index and add to tree
    #     Go to the righter most array

    #     Find middle index of the array (right middle index if array is even)
    #     Pop index and add to tree
    #     Go to righter most array

    #     Repeat steps until all elements are added to tree; tree will be even in height
    #     """
    #     return 0
    
    def bad_array_to_tree():
        tree.self.value = None
        #Root
        tree = TreeNode(array[len(array)//2])

        #Right
        for i in range(len(array)//2 + 1, len(array)):
            tree.insert(array[i])

        #Left
        for j in range(0, len(array)//2):
            tree.insert (array[j])

        return tree
    
    def rotate_left():
        """
        a = self.value
        b = self.right.value
        A = self.left
        B = self.right.left
        C = self.right.right
         
        Turns into 

        self.value = b
        self.left = Node(a)
        self.left.left = A
        self.left.right = B
        self.right = C
        """

array = [1, 12, 31, 14, 51, 16, 71, 18, 91]
root = TreeNode.array_to_tree(array)
root.inorder_traversal()
print("Done!")


