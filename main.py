from bintree import Tree
import numpy as np

def main():
    some_tree = Tree(12)
    some_list = np.random.randint(101, size = 18)
    some_tree.add_list(some_list)
    print(some_tree)
    
main()