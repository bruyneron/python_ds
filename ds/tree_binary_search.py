class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.data == value:
            return 
        
        if value < self.data:
            if self.left:
                self.left.insert(value)    
            else:
                self.left = BSTNode(value)
        
        if value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
    
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def delete(self):
        # No child
        # 1 child - left/right
        # 2 children - 2 ways. 
        #               insert max of left subtree
        #               insert min of right subtree
        pass
    
    def invert(self):
        if self: 
            # Can't create empty BST with this implementation. So this is not required.
            # This BST implementatio will make sure that BST node is created with atleast one node
            # Useful when --> invert(node): if node: pass 
            if self.left is None and self.right is None: 
                # This check is not required. Even if this check doesn't exitst code will work.
                # But this will speed up the leaf node computations and won't reverse left(none) and right(none) of leaf node
                return

            self.left, self.right = self.right, self.left
            if self.left:
                self.left.invert()
            if self.right:
                self.right.invert()

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data
    
    def sum(self):
        sum = 0

        sum += self.data
        if self.left:
            sum += self.left.sum()
        if self.right:
            sum += self.right.sum()

        return sum 
    
    def inorder_traversal(self):
        # if self.left:
        #     self.left.inorder_traversal()
        
        # print(self.data)

        # if self.right:
        #     self.right.inorder_traversal()

        elements = []

        if self.left:
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def preorder_traversal(self):
        # [ROOT 1st-> 5, 3, 1, 2, 4, 7]
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.preorder_traversal()
        
        if self.right:
            elements += self.right.preorder_traversal()
        
        return elements
    
    def postorder_traversal(self):
        # [2, 1, 4, 3, 7, 5 <-- ROOT Last]
        elements = []
        
        if self.left:
            elements += self.left.postorder_traversal()
        
        if self.right:
            elements += self.right.postorder_traversal()
        
        elements.append(self.data)

        return elements


if __name__ == '__main__':
    root = BSTNode(5)
    root.insert(3)
    root.insert(7)
    root.insert(1)
    root.insert(4)
    root.insert(2)
    print(root.inorder_traversal())
    print(root.preorder_traversal())
    print(root.postorder_traversal())
    print(root.search(0))
    print(root.search(2))
    print(root.find_max())
    print(root.find_min())
    print(root.sum())
    print('Inverting tree for fun and printing inorder traversal - ')
    print('CAUTION: This is just an experiment. Inverting BST in-place, will violate the basic properties of a BST')
    root.invert()
    print(root.inorder_traversal())

    another_root = BSTNode('test')
    print(another_root.inorder_traversal())
