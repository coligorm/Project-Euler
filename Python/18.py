'''
Maximum Path Sum I

Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 =23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

# Source: https://www.codecademy.com/learn/learn-data-structures-and-algorithms-with-python/modules/trees/cheatsheet

class TreeNode:
    def __init__(self, value):
        self.value = value # data
        self.children = [] # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        self.children.append(child_node) 

    def get_all_routes(self, path=None):
        if path is None:
            path = []
        path = path + [int(self.value)]
        if not self.children:
            return [path]
        routes = []
        for child in self.children:
            routes.extend(child.get_all_routes(path))
        return routes

def read_file(filename):
    list_of_lists = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(num) for num in line.strip().split()]
            list_of_lists.append(row)
    return list_of_lists

def build_tree(l):
    # Create TreeNode objects for each value
    nodes = [[TreeNode(str(value)) for value in row] for row in l]
    # Link children
    for i in range(len(nodes) - 1):
        for j in range(len(nodes[i])):
            nodes[i][j].add_child(nodes[i+1][j])
            nodes[i][j].add_child(nodes[i+1][j+1])
    return nodes[0][0]  # Return the root node

def find_max(l):
    current_max = 0
    for route in l:
        total = sum(route)
        if total > current_max:
            current_max = total
    return current_max
        
def main():
    root = build_tree(input)
    routes = root.get_all_routes()
    print(find_max(routes))

    
if __name__ == "__main__":
    test = read_file('input_files/18-test.txt')
    input = read_file('input_files/18-input.txt')
  
    main()