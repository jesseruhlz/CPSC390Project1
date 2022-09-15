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

#Create an object of the tree
romania = Tree()

#create nodes for romania tree
root1 = Node("Arad")
Timi = Node("Timisoara")
Lugoj = Node("Lugoj")
Mehadia = Node("Mehadia")
Drobeta = Node("Drobeta")
Zerind = Node("Zerind")
Oradea = Node("Oradea")
Sibiu = Node("Sibiu")
Craiova = Node("Craiova")
Rimnicu = Node("Rimnicu Vilcea")
Fagaras = Node("Fagaras")
Pitesti = Node("Pitesti")
Bucharest = Node("Bucharest")
Giurgiu = Node("Giurgiu")
Urziceni = Node("Urziceni")
Vaslui = Node("Vaslui")
Iasi = Node("Iasi")
Neamt = Node("Neamt")
Hirsova = Node("Hirosova")
Eforie = Node("Eforie")

romania.addRoot(root1)
romania.addNode(Timi,root1,118)
romania.addNode(Zerind,root1,75)
romania.addNode(Sibiu,root1,140)
romania.addNode(Lugoj,Timi,111)
romania.addNode(Oradea,Zerind,71)
romania.addNode(Sibiu,Oradea,151)
romania.addNode(Mehadia,Lugoj,70)
romania.addNode(Drobeta,Mehadia,75)
romania.addNode(Craiova,Drobeta,120)
romania.addNode(Craiova,Rimnicu,146)
romania.addNode(Rimnicu,Sibiu,80)
romania.addNode(Fagaras,Sibiu,99)
romania.addNode(Pitesti,Craiova,138)
romania.addNode(Pitesti,Rimnicu,97)
romania.addNode(Bucharest,Fagaras,211)
romania.addNode(Bucharest,Pitesti,101)
romania.addNode(Giurgiu,Bucharest,90)
romania.addNode(Urziceni,Bucharest,85)
romania.addNode(Hirsova,Urziceni,98)
romania.addNode(Eforie,Hirsova,86)
romania.addNode(Vaslui,Urziceni,142)
romania.addNode(Iasi,Vaslui,92)
romania.addNode(Neamt,Iasi,87)

romania.depthFirstSearch(root1,Bucharest)
print("Expanded node: " + str(romania.visited))
print("The resulting path: " + str(romania.path))
