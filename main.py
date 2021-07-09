import Bitmap as bmp
import FileHandling as FileH


if __name__ == "__main__":
    bitmap = bmp.Bitmap("Bitmap/test_case_4x4.bmp")
    print(bitmap.toArray())

    file = FileH.FileHandling("Text/input.txt")
    start, goal, m = file.readData()
    arr = []
    arr.append(start.getCoordinates())
    arr.append(goal.getCoordinates())
    arr.append(m)
    file = FileH.FileHandling("Text/output.txt")
    file.writeData(arr)