from tEST2 import *

class Nodes():
    def Node(self, position, ID):
        self.Id = ID
        self.GScore = 0
        self.HScore = 0
        self.FScore = 0
        self.position = position

class Graph():
    def Graph(self, nodes):
        nodes = []
 
class CalcGScore():
    def CalcgScore(self, current, neighbor):
        #instead of making 2, verthori is the cost as vertical and horizontal
        verthori = 10
        diagonal = 14
        if (current[0] + 1, current[1]) or (current[0], current[1] + 1) or (current[0] - 1, current[1]) or (current[0], current[1] - 1):
            GScore = verthori
        if (current[0] + 1, current[1] + 1) or (current[0] - 1, current[1] - 1) or (current[0] + 1, current[1] - 1) or (current[0] - 1, current[1] + 1):
            GScore = diagonal

class CalcHScore():
    def CalchScore(self, node, goal):
        HScore = abs(node.posx - goal.posx) + abs(node.posy - goal.posy)

class CalcFScore():
    def CalcfScore(self, node):
        node.FScore = node.GScore + node.HScore

class GetNeighbors():
    def Getneighbors(self, node, nodes):
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

class AStar():
    def Astar(self, start, goal, graph):
        #All the stuff
        #returns a list ehich is the path returned
        graph = list(GRAPH)
        openList = []
        closedList = []
        pathway = []
        openList.append(start)
        openList.sort(key=lambda x: x.f)