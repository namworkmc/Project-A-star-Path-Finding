import numpy as np
import math


class Coordinate:
    ############################# Attributes #############################
    next = None

    ############################# Constructor #############################
    def __init__(self, x, y):
        """
        Truyền vào x và y
        """
        self.x = x
        self.y = y

    ############################# Methods #############################

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neq__(self, other):
        return self.x != other.x or self.y != other.y

    def setNext(self, other):
        self.next = other

    def getNext(self):
        return self.next

    def isMoveable(firstCoordinate, secondCoordinate, m: int, bitmapArray: np.ndarray) -> bool:
        """
        Hàm trả về chênh lệch độ cao giữa 2 toạ độ

        Params:
                Coordinate: toạ độ 1
                Coordinate: toạ độ 2
                int: tham số m
                Array: ma trận pixel

        Return:
                int: chênh lệch độ cao
        """

        a1 = int(bitmapArray[firstCoordinate.x][firstCoordinate.y])
        a2 = int(bitmapArray[secondCoordinate.x][secondCoordinate.y])
        delta = a1 - a2

        firstCondition = abs(firstCoordinate.x - secondCoordinate.x) <= 1
        secondCondition = abs(firstCoordinate.y - secondCoordinate.y) <= 1
        thirdCondition = abs(delta) <= m

        return firstCondition and secondCondition and thirdCondition

    def getDistance(firstCoordinate, secondCoordinate, bitmapArray: np.ndarray) -> float:

        a1 = int(bitmapArray[firstCoordinate.x][firstCoordinate.y])
        a2 = int(bitmapArray[secondCoordinate.x][secondCoordinate.y])
        delta = a1 - a2
        sgn = np.sign(delta)

        distance: float = math.sqrt(
            (secondCoordinate.x - firstCoordinate.x) ** 2 + (secondCoordinate.y - firstCoordinate.y) ** 2)
        k: float = (float(1/2) * sgn + 1) * abs(delta)

        return distance + k