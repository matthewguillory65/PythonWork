from tEST2 import *

class Nodes(object):
    def __init__(self, ID, position):
        self.Id = ID
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.walkable = True
        self.position = position
        self.parent = None

#def Graph(self, nodes):
#nodes = []

def CalcGScore(current, neighbor):
    #Gets the g score; Cost to move from the starting point A to a given square on the grid,
    #following the the generated path to get there.
    #instead of making 2, verthori is the cost as vertical and horizontal
    if (current.position[0] == neighbor.position[0]) or (currnet.position[1] == neighbor.position[1])
        g = current.g + 10
    else:
        g = current.g + 14
    

def CalcHScore(node, goal):
  #Gets the h score; the estimated movement cost to move from that given square on the
  #grid to the final destination, point B
  HScore = abs(node.posx - goal.posx) + abs(node.posy - goal.posy)

def CalcFScore(node):
  #Gets the f score; G score + H score
  node.FScore = node.GScore + node.HScore

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