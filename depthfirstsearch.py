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
    def _init_(self, state, edgeWeight = 0):
        self.state = state # Letter
        self.edgeWeight = edgeWeight # Cost from parent to child Node
        self.children = []

    def addChild(self, childNode, edgeWeight):
        childNode.parent = self
        childNode.edgeWeight = edgeWeight
        self.children.append(childNode)

# Tree
class Tree():
    def _init_(self):
        self.root = None
        self.path = []
        self.visited = []
        self.destinationFound = False

    # add the root to the Tree
    def addRoot(self, rootNode):
        self.rootNode = rootNode

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
            self.depthFirstSearch(n, destintaion)
            # if currentNode is not in path then remove it
            if (not self.destinationFound):
                self.path.pop()
