# CPSC390Project1
This project uses one of the algorithms (depth-first, breadth-first, or uniform cost search) to find the goal state from a tree.
/**
  * Full name: Jesse Ruhl, Everett Prussak
  * Course number: CPSC 390
  * Project 1
*/
# Instructions
Task:
(1) In the figure 1, use one of the algorithms, depth-
first search, breadth-first search, uniform cost search
to find the Goal (start state: S, goal state:G), print the
solution path.
(2) Use your algorithm to search the Romania
map(Figure 2) (start state: Arad, goal state:
Bucharest), print the solution path.

# Report
For this project, we decided to approach both the tree and the map using a depth first search algorithm. We used the functions provided by aima-python to create this project and create our algorithm. We first create a node in our project that we use to hold each state in the map/tree, where each node has a weight, is added to an array, and has an addChild function. We then used the Tree class to initialize the tree by adding a root and also being able to add nodes. From there, we created the depth first search function and created the respective tree and map.
