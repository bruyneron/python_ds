class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
    
    def get_level(self):
        level = 0
        parent = self.parent

        while parent:
            level += 1
            parent = parent.parent
        
        return level
    
    def print_tree(self):       
        # print(self.data)
        # for child in self.children:
        #     child.print_tree()
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
   

if __name__ == '__main__':
    ceo = TreeNode('CEO')
    
    cto = TreeNode('CTO')

    director = TreeNode('Director')

    manager1 = TreeNode('Manager1')
    manager1.add_child(TreeNode('Employee 1'))
    manager1.add_child(TreeNode('Employee 2'))
    manager1.add_child(TreeNode('Employee 3'))

    manager2 = TreeNode('Manager2')
    manager2.add_child(TreeNode('Employee 1'))
    manager2.add_child(TreeNode('Employee 2'))
    manager2.add_child(TreeNode('Employee 3'))

    director.add_child(manager1)
    director.add_child(manager2)
    
    cto.add_child(director)

    cfo = TreeNode('CFO')
    director = TreeNode('Director')

    manager1 = TreeNode('Manager1')
    manager1.add_child(TreeNode('Employee 1'))
    manager1.add_child(TreeNode('Employee 2'))
    manager1.add_child(TreeNode('Employee 3'))

    manager2 = TreeNode('Manager2')
    manager2.add_child(TreeNode('Employee 1'))
    manager2.add_child(TreeNode('Employee 2'))
    manager2.add_child(TreeNode('Employee 3'))

    director.add_child(manager1)
    director.add_child(manager2)
    
    cfo.add_child(director)

    ceo.add_child(cto)
    ceo.add_child(cfo)

    ceo.print_tree()

    # cfo.print_tree()
    print(manager2.get_level())