from tEST2 import *


class Nodea(object):
    def __init__(self, ID, position):
        self.Id = ID
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.adjacents = []
        self.walkable = True
        self.position = position
        self.parent = None

    def __getitem__(self, key):
        return self.position[key]


class Grid(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.nodes = []

    def generatenodes(self):
        count = 0
        for i in range(self.cols):
            for j in range(self.rows):
                count += 1
                newnode = Node(count, [i, j])


def CalcGScore(current, neighbor):
    # Gets the g score; Cost to move from the starting point A to a given square on the grid,
    # following the the generated path to get there.
    tentative = 0
    if (current.pos[0] == neighbor.pos[0]) or (current.pos[1] == neighbor.pos[1]):
        tentative = current.g + 10
    else:
        tentative = current.g + 14
    if neighbor.parent is None:
        neighbor.g = tentative
        neighbor.parent = current
    if tentative < current.g:
        neighbor.g = tentative
        neighbor.parent = current
    return current.g


def CalcHScore(node, goal):
    # Gets the h score; the estimated movement cost to move from that given square on the
    # grid to the final destination, point B
    node.h = (abs(node.pos[0] - goal.pos[0]) +
              abs(node.pos[1] - goal.pos[1])) * 10
    return node.h


def CalcFScore(node):
    # Gets the f score; G score + H score
    node.f = node.g + node.h
    return node.f


def Getneighbors(node, graph):
    # The node needs to be in the graph and if it is, get neighbors
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
    # returns a list ehich is the path returned
    graph = list(GRAPH)
    openList = []
    path = []
    closedList = []
    openList.append(start)
    openList.sort(key=lambda x: x.f)

    while openList:
        currentNode = openList[0]
        openList.remove(currentNode)
        closedList.append(currentNode)
        if currentNode == goal:
            path = Retrace(currentNode)
            return path
        neighborsa = getneighbors(currentNode, graph)
        for m in neighborsa:
            if m in closedList or not m.walkable:
                continue
            tentative_g = m.g + CalcGScore(currentNode, m)
            if m not in openList:
                openList.append(m)
            elif tentative_g >= m.g:
                continue
            m.parent = currentNode
            CalcGScore(start, goal)
            CalcHScore(currentNode, goal)
            CalcFScore(currentNode)
    return path
    # for neighbors in currentNode.adjacents:
    #     if neighbors not in closedList and neighbors.walkable:
    #         if neighbors not in openList:
    #             openList.append(neighbors)
    #         CalcGScore(start, goal)
    #         CalcHScore(currentNode, goal)
    #         CalcFScore(currentNode)
    #         neighbors.parent = currentNode


def Retrace(node):
    final_path = []
    parentNode = node
    while parentNode is not None:
        final_path.append(parentNode)
        parentNode = parentNode.parent
    return final_path
