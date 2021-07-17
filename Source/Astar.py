import numpy as np
import sympy
from Coordinate import Coordinate
from FileHandling import FileHandling
from _Bitmap import Bitmap
from queue import PriorityQueue


def getSuccessor(bitmapArray, row, col, G_Score, current, visited, visitor, m):
    Successor = []
    for new_coordinate in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if (current.x + new_coordinate[0] > row - 1 or current.x + new_coordinate[0] < 0 or current.y + new_coordinate[1] > col - 1 or current.y + new_coordinate[1] < 0):
            continue

        if(visited[current.x + new_coordinate[0]][current.y + new_coordinate[1]] != 1):
            visitor += 1
            visited[current.x + new_coordinate[0]
                    ][current.y + new_coordinate[1]] = 1

        new_coor = Coordinate(
            current.x + new_coordinate[0], current.y + new_coordinate[1])

        if(current.isMoveable(new_coor, m, bitmapArray) == True):
            Successor.append(new_coor)

    return Successor, visitor


def heuristicManhattan(firstCoordinate: Coordinate, secondCoordinate: Coordinate, m: int) -> float:
    k = abs(m - (abs(firstCoordinate.x - secondCoordinate.x) +
            abs(firstCoordinate.y - secondCoordinate.y)))
    while not sympy.isprime(k):
        k += 1

    # return abs(firstCoordinate.x - secondCoordinate.x) + abs(firstCoordinate.y - secondCoordinate.y) + k
    return abs(firstCoordinate.x - secondCoordinate.x) + abs(firstCoordinate.y - secondCoordinate.y)


def Astar(bitmapArray: np.ndarray, start, goal, m):
    row = len(bitmapArray)
    col = len(bitmapArray[0])
    count = 0

    visited = [[0 for _ in range(row)] for _ in range(col)]

    open_lst = PriorityQueue()
    open_lst.put((heuristicManhattan(start, goal, m), count, start))
    count += 1

    G_Score = [[np.inf for _ in range(row)] for _ in range(col)]
    G_Score[start.x][start.y] = 0
    visited[start.x][start.y] = 1
    visitor = 1

    while open_lst.empty() == False:
        current = open_lst.get()[2]
        if(current == goal):
            totalCost = G_Score[current.x][current.y]
            path = []
            while (current != start):
                path.append(current)
                current = current.getNext()
            path.append(current)
            print("Done!")
            return path[::-1], totalCost, visitor

        Successor, visitor = getSuccessor(
            bitmapArray, row, col, G_Score, current, visited, visitor, m)

        for succ in Successor:
            succ_current_cost = G_Score[current.x][current.y] + \
                current.getDistance(succ, bitmapArray)
            if(succ_current_cost < G_Score[succ.x][succ.y]):
                G_Score[succ.x][succ.y] = succ_current_cost
                H_Score = heuristicManhattan(succ, goal, m)
                open_lst.put((G_Score[succ.x][succ.y] + H_Score, count, succ))
                count += 1
                succ.setNext(current)

    print("Cannot find path!")
    return None, None, visitor


def start():

    ## INPUT ##
    bitmap = Bitmap("Bitmap/map.bmp")
    arr = bitmap.toArray()

    file = FileHandling("Text/input.txt")
    start, goal, m = file.readData()

    result, cost, point = Astar(arr, start, goal, m)
    print(cost)
    print(point)

    ## OUTPUT ##
    file = FileHandling("Text/output.txt")
    arr = []
    arr.append(cost)
    arr.append(point)
    file.writeData(arr)

    bitmap.changeColorOfPixel("Bitmap/map_update.bmp", result)