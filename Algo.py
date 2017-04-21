#from tEST2 import *

class Node(object):
    def __init__(self, ID, position):
        self.Id = ID
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.walkable = True
        self.position = position
        self.parent = None

class Grid(object):
    def __init__(self, nodes, rows, cols):
        self.rows = rows
        self.cols = cols

    def generatenodes(self):
        

#def Graph(self, nodes):
#nodes = []

def CalcGScore(current, neighbor):
    #Gets the g score; Cost to move from the starting point A to a given square on the grid,
    #following the the generated path to get there.
    tentative = 0
    if (current.position[0] == neighbor.position[0]) or (current.position[1] == neighbor.position[1]):
        tentative = current.g + 10
    else:
        tentative = current.g + 14
    if neighbor.parent is None:
        neighbor.g = tentative
        neighbor.parent = current
    if tentative < current.g:
        neighbor.g = tentative
        neighbor.parent = current

def CalcHScore(node, goal):
  #Gets the h score; the estimated movement cost to move from that given square on the
  #grid to the final destination, point B
  node.h = (abs(node.position[0] - goal.position[0]) + abs(node.position[1] - goal.position[1])) * 10

def CalcFScore(node):
  #Gets the f score; G score + H score
  node.f = node.g + node.h

def Getneighbors(node, graph):
  #The node needs to be in the graph and if it is, get neighbors
  current = node
  right = (current[0] + 1, current[1])
  left = (current[0] - 1, current[1])
  up = (current[0], current[1] + 1)
  down = (current[0], current[1] - 1)
  up_right = (current[0] + 1, current[1] + 1)
  up_left = (current[0] - 1, current[1] + 1)
  down_right = (current[0] + 1, current[1] - 1)
  down_left = (current[0] - 1, current[1] - 1)
  direc = [right, left, up, down, up_right, up_left, down_right, down_left]
  for i in graph:
      for position in graph:
          if i[0] == position[0] and i[1] == position[1]:
              node.neighbors.append(i)
  return node.neighbors

def Astar(start, goal, graph):
    #returns a list ehich is the path returned
    graph = list(GRAPH)
    openList = []
    closedList = []
    currentNode = start
    openList.append(currentNode)
    openList.sort(key=lambda x: x.f)

def Retrace(node):
    final_path = []
    parentNode = node
    while parentNode is not None:
        final_path.append(parentNode)
        parentNode = parentNode.parent
    return final_path