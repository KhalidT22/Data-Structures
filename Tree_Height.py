import sys

data = list(map(int, sys.stdin.read().split()))

class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes
        self.parent = -1


    def add_child(self, child_node):
        # creates parent-child relationship
        self.children.append(child_node)


    def add_parent(self, parent):
        self.parent = parent

def tree_height(data):
    n = data[0]
    nodes = data[1:]
    tree = []
    for i in range(0,n):
        tree.append(TreeNode(i))
    for i in range(n):

        if nodes[i] == -1:
            root_index = i

            continue
        else:

            tree[i].add_parent(nodes[i])
            tree[nodes[i]].add_child(i)
    '''
    for i in range(0,n):
        print("node ",i ,": parent:",tree[i].parent)
    print("############")
    for i in range(0,n):
        print("node ",i ,": children:",tree[i].children)
    '''

    height_array = [None for i in range(n)]
    height_array[root_index] = 1

    #print("tree: ",tree)
    '''
    for i in range(n):
        print("i: ",i, " value:",tree[i].value)
    '''
    for i in range(n):
        if i == root_index:
            continue
        height = 0
        current = i
        while current != root_index:
            height += 1
            parent = tree[current].parent
            if height_array[parent]:
                height_array[i] = height_array[parent] +height
                break
            current = parent
    #print(height_array)
    print(max(height_array))

tree_height(data)
