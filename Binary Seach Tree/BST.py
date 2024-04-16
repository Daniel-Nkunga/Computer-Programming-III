import time
import random

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
        if self.height_factor() > 1:
            self.rotate_left()
        if self.height_factor() <= -1:
            self.rotate_right()

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
        if self.height_factor() > 1:
            self.rotate_left()
        if self.height_factor() <= -1:
            self.rotate_right()
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

    def get_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return 1 +max(left_height, right_height)
    
    def height_factor(self):
        right_height = self.right.get_height() if self.right else 0
        left_height = self.left.get_height() if self.left else 0
        return right_height - left_height


def main():
    start = time.time()
    n = 0
    tree = TreeNode(random.randint(1, 2**32))
    for i in range(2**15 + 3):
        if i == 2**n:
            print(f"{i}, {(time.time() - start):.10}")
            n = n+1
        tree.insert(random.randint(1, 2**32))
    # tree.preorder_traversal()
    # print()
    # print(tree.height_factor())
    print(time.time() - start)


if __name__ == "__main__":
    main()