from Coordinate import Coordinate
from FileHandling import FileHandling
from Coordinate import Coordinate
from Bitmap import Bitmap

def test():
    # bitmap = Bitmap("Bitmap/test_case_4x4.bmp")
    # arr = bitmap.toArray()
    # print(arr)
    # print(bitmap.getHeight(), bitmap.getWidth())

    # file = FileHandling("Text/input.txt")
    # start, goal, m = file.readData()
    # arr = []
    # arr.append(start.getCoordinate())
    # arr.append(goal.getCoordinate())
    # arr.append(m)
    # file = FileHandling("Text/output.txt")
    # file.writeData(arr)

    # bitmap = Bitmap("Bitmap/test_case_4x4.bmp")
    # bitmap.toArray()
    # list = []
    # list.append(Coordinate(0, 0))
    # list.append(Coordinate(1, 1))
    # list.append(Coordinate(2, 2))
    # list.append(Coordinate(3, 3))
    # bitmap.changeColorOfPixel("Bitmap/test_case_4x4_update.bmp", list)

    bitmap = Bitmap("Bitmap/test_case_4x4.bmp")
    arr = bitmap.toArray()
    start = Coordinate(2, 3)
    goal = Coordinate(3, 2)
    print(arr)
    print(start.isMoveable(goal, 51, arr))
    print(start.getDistance(goal, arr))

    return

if __name__ == "__main__":
    test()
