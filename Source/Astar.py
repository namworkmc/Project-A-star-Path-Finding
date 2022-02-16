import numpy as np
import math
import sympy
import time

from Coordinate import Coordinate
from FileHandling import FileHandling
from _Bitmap import Bitmap
from queue import PriorityQueue


def getSuccessor(bitmapArray, row, col, G_Score, current: Coordinate, visitor, m):
    Successor = []
    for new_coordinate in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if (current.x + new_coordinate[0] > row - 1 or current.x + new_coordinate[0] < 0 or current.y + new_coordinate[1] > col - 1 or current.y + new_coordinate[1] < 0):
            continue

        if(G_Score[current.x + new_coordinate[0]][current.y + new_coordinate[1]] == np.inf):
            visitor += 1

        new_coor = Coordinate(
            current.x + new_coordinate[0], current.y + new_coordinate[1])

        if(current.isMoveable(new_coor, m, bitmapArray) == True):
            Successor.append(new_coor)

    return Successor, visitor


def heuristic(firstCoordinate: Coordinate, secondCoordinate: Coordinate, m: int, index: int = 0) -> float:
    if(index == 1):
        ## Manhattan ##
        return abs(firstCoordinate.x - secondCoordinate.x) + abs(firstCoordinate.y - secondCoordinate.y)
    elif(index == 2):
        ## Euclid ##
        return math.sqrt((firstCoordinate.x - secondCoordinate.x) ** 2 + (firstCoordinate.y - secondCoordinate.y) ** 2)
    elif(index == 3):
        ## Circle Area ##
        return abs((math.sqrt((firstCoordinate.x - secondCoordinate.x) ** 2 + (firstCoordinate.y - secondCoordinate.y) ** 2) / 2) * math.pi)
    elif(index == 4):
        ## Custom Manhattan ##
        k = abs(m - (abs(firstCoordinate.x - secondCoordinate.x) +
                abs(firstCoordinate.y - secondCoordinate.y)))
        while not sympy.isprime(k):
            k += 1

        return abs(firstCoordinate.x - secondCoordinate.x) + abs(firstCoordinate.y - secondCoordinate.y) + k
    elif(index == 5):
        ## Custom Euclid ##
        k = math.ceil(abs(m - (math.sqrt((firstCoordinate.x - secondCoordinate.x) ** 
                        2 + (firstCoordinate.y - secondCoordinate.y) ** 2))))
        while not sympy.isprime(k):
            k += 1

        return math.sqrt((firstCoordinate.x - secondCoordinate.x) ** 2 + (firstCoordinate.y - secondCoordinate.y) ** 2) + k


def Astar(bitmapArray: np.ndarray, start, goal, m, index_heuristic):
    """
    index = 1: Manhattan
    index = 2: Euclid
    index = 3: Circle Area
    index = 4: Custom Manhattan
    index = 5: Custom Euclid
    """

    row = len(bitmapArray)
    col = len(bitmapArray[0])

    count = 0
    open_lst = PriorityQueue()
    open_lst.put((heuristic(start, goal, m, index_heuristic), count, start))
    count += 1

    G_Score = [[np.inf for _ in range(col)] for _ in range(row)]
    G_Score[start.x][start.y] = 0
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
            bitmapArray, row, col, G_Score, current, visitor, m)

        for succ in Successor:
            succ_current_cost = G_Score[current.x][current.y] + \
                current.getDistance(succ, bitmapArray)
            if(succ_current_cost < G_Score[succ.x][succ.y]):
                G_Score[succ.x][succ.y] = succ_current_cost
                H_Score = heuristic(succ, goal, m, index_heuristic)
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

    print("1: Manhattan")
    print("2: Euclid")
    print("3: Circle Area")
    print("4: Custom Manhattan")
    print("5: Custom Euclid")

    choice = int(input("Choose: "))

    prev = time.time()
    result, distance, totalPoint = Astar(arr, start, goal, m, choice)
    current = time.time()
    print("Total distance:" + str(distance))
    print("Total points: " + str(totalPoint))
    print("Time cost: " + str(abs(current - prev)))

    ## OUTPUT ##
    textOutputPath = "Text/output" + str(choice) + ".txt"
    file = FileHandling(textOutputPath)
    arr = []
    arr.append(distance)
    arr.append(totalPoint)
    file.writeData(arr)

    if result != None:
        bitmapOutputPath = "Bitmap/map" + str(choice) + ".bmp"
        bitmap.changeColorOfPixel(bitmapOutputPath, result)
