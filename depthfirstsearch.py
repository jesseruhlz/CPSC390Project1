# Group members
# Jesse Ruhl
# Everett Prussak
# CPSC 390
# Project 1

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
