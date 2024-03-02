class Tree:
    def __init__(self, root):
        self.root = self.Node(root, 0)
        self.max_height = 0


    def add_single_value(self, elem):
        self.Node.insert(self.root, elem)
    
    
    def add_list(self, val_list):
        for elem in val_list:
            self.Node.insert(self.root, elem)

     
    def __str__(self):
        tree_string = ""
        tree_string = f"{self.root}" + "\n"
        old_elements = [self.root]
        print(self.Node.find_height(self,self.root))
        for h in range(self.Node.find_height(self, self.root)):
            new_elements = []
            for element in old_elements:
                if element.left:
                    new_elements.append(element.left)
                else:
                    new_elements.append(None)
                if element.right:
                    new_elements.append(element.right)
                else:
                    new_elements.append(None)
            for element in new_elements:
                tree_string += f"{element}"
            tree_string += "\n"
            old_elements = new_elements
        tree_string.center((self.Node.find_height(self, self.root) * 2) + 1)
        return tree_string
    

    class Node:
        def __init__(self, value, height):
            self.value = value
            self.left = None
            self.right = None
            self.height = height
            self.counter = 1
            
            
        def insert(self, new_elem):
            if self.value > new_elem:
                if self.left == None:
                    self.left = Tree.Node(new_elem, self.height + 1)
                else:
                    self.left.insert(new_elem)   
            elif self.value < new_elem:
                if self.right == None:
                    self.right = Tree.Node(new_elem, self.height +1)
                else:
                    self.right.insert(new_elem)
            else: 
                self.counter += 1
    
        
        def find_height(self, root):
            if root.left:
                max_left = self.Node.find_height(self, root.left)
            else: max_left = root.height
            if root.right:
                max_right = self.Node.find_height(self, root.right)
            else: max_right = root.height
            return max(max_left, max_right)
        
        def __str__(self):
            return f'{self.value}({self.counter})'
        
