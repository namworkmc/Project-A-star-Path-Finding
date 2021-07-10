class Coordinate:
    x = 0
    y = 0

    def __init__(self, x, y):
        """
        Truyền vào x và y
        """
        self.x = x
        self.y = y

    def getCoordinate(self):
        """
        Phương thức trả về toạ độ x và toạ độ y

        Returns:
               x: toạ độ x
               y: toạ độ y
        Rtype:
              int
        """
        return self.x, self.y
