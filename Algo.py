from tEST2 import *
import pygame

def Algorithem(start, end, graph):
    
    openList = []
    closedList = []

    if openList and currentnode != End:
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