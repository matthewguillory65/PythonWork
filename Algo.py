from tEST2 import *
import pygame
from drawablenode import *

def Algorithem(start, end, graph):
    ROWS = 34
    COLS = 18
    NODES = {}
    for i in range(ROWS):
        for j in range(COLS):
            NODES[str([i, j])] = DrawableNode(i, j)
    start = NODES[str([0, 0])]
    openList = []
    closedList = []
    currentnode = start

    currentnode.g = 1
    currentnode.h = abs(currentnode.posx - end.posx) + abs(currentnode.posy - end.posy)
    currentnode.f = currentnode.g + currentnode.h
    
    openList.append(currentnode)

    if openList and currentnode != end:
        currentnode = openList[0]

        openList.remove(currentnode)
        closedList.append(currentnode)

        for neighbors in currentnode.adjacents:
            if neighbors not in closedList and neighbors.walkable:
                if neighbors not in openList:
                    openList.append(neighbors)
                neighbors.g = 1 + currentnode.g
                neighbors.h = abs(neighbors.posx - End.posx) + abs(neighbors.posy - End.posy)
                neighbors.f = neighbors.g + neighbors.h
                if neighbors.parent:
                    if neighbors.parent.g > currentnode.g:
                        neighbors.parent = currentnode
                else:
                    neighbors.parent = currentnode

        openList.sort(key = lambda n: n.f)