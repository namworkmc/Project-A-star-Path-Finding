import numpy as np
import math

class Coordinate:
    ############################# Attributes #############################

    # Trục x 
    __x = 0

    # Trục y #
    __y = 0

    ############################# Constructor #############################
    def __init__(self, x, y):
        """
        Truyền vào x và y
        """
        self.__x = x
        self.__y = y

    ############################# Methods #############################
    def getCoordinate(self):
        """
        Phương thức trả về toạ độ x và toạ độ y

        Returns:
               x: toạ độ x
               y: toạ độ y
        Rtype:
              int
        """
        return self.__x, self.__y
    
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

        x1, y1 = firstCoordinate.getCoordinate()
        x2, y2 = secondCoordinate.getCoordinate()

        a1 = int(bitmapArray[y1][x1])
        a2 = int(bitmapArray[y2][x2])
        delta = a1 - a2

        firstCondition = abs(x1 - x2) <= 1
        secondCondition = abs(y1 - y2) <= 1
        thirdCondition = abs(delta) <= m

        return firstCondition and secondCondition and thirdCondition
    
    def getDistance(firstCoordinate, secondCoordinate, bitmapArray: np.ndarray) -> float:
        x1, y1 = firstCoordinate.getCoordinate()
        x2, y2 = secondCoordinate.getCoordinate()

        a1 = int(bitmapArray[y1][x1])
        a2 = int(bitmapArray[y2][x2])
        delta = a1 - a2
        sgn = np.sign(delta)

        distance : float = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        k : float = (float(1/2) * sgn + 1) * abs(delta)

        return distance + k