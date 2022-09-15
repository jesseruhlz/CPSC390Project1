# Group members
# Jesse Ruhl
# Everett Prussak
# CPSC 390
# Project 1

# References
# https://github.com/aimacode
# https://github.com/aimacode/aima-python/blob/master/search.ipynb


# Node
class Node():
    def __init__(self, state, edgeWeight=0):
        self.state = state # Letter
        self.edgeWeight = edgeWeight # Cost from parent to self
        self.children = []

    def addChild(self, childNode, edgeWeight):
        childNode.parent = self
        childNode.edgeWeight = edgeWeight
        self.children.append(childNode)

# Tree
class Tree():
    def __init__(self):
        self.root = None
        self.path = []
        self.visited = []
        self.destinationFound = False

    # add the root to the Tree
    def addRoot(self, rootNode):
        self.root = rootNode

    # add the node to the Tree
    def addNode(self, childNode, parentNode, edgeWeight):
        parentNode.addChild(childNode, edgeWeight)

    def depthFirstSearch(self, currentNode, destination):
        if (self.destinationFound):
            return

        # add currentNode to visisted arr and path arr
        self.visited.append(currentNode.state)
        self.path.append(currentNode.state)

        if (currentNode.state == destination.state):
            self.destinationFound = True
            return

        # add children nodes to frontier
        for n in currentNode.children:
            self.depthFirstSearch(n, destination)
            # if currentNode is not in path then remove it
            if (not self.destinationFound):
                self.path.pop()

# create an object of the Tree
tree = Tree()

# create nodes for Tree
root = Node("S")
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
g = Node("G")

tree.addRoot(root)
tree.addNode(a, tree.root, 3)
tree.addNode(b, tree.root, 1)
tree.addNode(c, tree.root, 8)
tree.addNode(d, a, 3)
tree.addNode(e, a, 7)
tree.addNode(g, a, 15)
tree.addNode(g, b, 20)
tree.addNode(g, c, 5)

tree.depthFirstSearch(tree.root, g)

print("Expanded node: " + str(tree.visited))
print("The resulting path: " + str(tree.path))
