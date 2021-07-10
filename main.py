from Coordinate import Coordinate
from Bitmap import Bitmap
from FileHandling import FileHandling
from Coordinate import Coordinate


if __name__ == "__main__":
    # bitmap = bmp.Bitmap("Bitmap/test_case_4x4.bmp")
    # arr = bitmap.toArray()
    # print(arr)
    # print(len(arr))
    # print(len(arr[0]))

    # file = FileHandling("Text/input.txt")
    # start, goal, m = file.readData()
    # arr = []
    # arr.append(start.getCoordinate())
    # arr.append(goal.getCoordinate())
    # arr.append(m)
    # file = FileHandling("Text/output.txt")
    # file.writeData(arr)

    bitmap = Bitmap("Bitmap/test_case_4x4.bmp")
    list = []
    list.append(Coordinate(0, 0))
    list.append(Coordinate(1, 1))
    list.append(Coordinate(2, 2))
    list.append(Coordinate(3, 3))
    bitmap.changeColorOfPixel("Bitmap/test_case_4x4_update.bmp", list)