

class leaf:
    def __init__(self, value, height):
        self.key = value
        self.left = None
        self.right = None
        self.height = 1 + max(self.right.height, self.left.height)    
    def __str__(self):
        return f'{self.value}'
        
class tree:
    def __init__(self, root):
        self.root = leaf(root, 0)
    def insert(self, value):
        if self.root.value < value:
            if self.left == None:
                self.root.left = leaf(value)
            else:
                self.left.insert()   
        elif self.root.value > value:
            if self.right == None:
                self.root.right = leaf(value)
            else:
                self.right.insert()
        else: print(f"duplicate values are currently not implemented. dropping {value}")
    def __str__(self):
        tree_string = str(self.root)
         
