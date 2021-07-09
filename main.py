import Bitmap as bmp
import FileHandling as FileH


if __name__ == "__main__":
    # bitmap = bmp.Bitmap("Bitmap/test_case_4x4.bmp")
    # print(bitmap.asArray())

    file = FileH.FileHandling("Text/input.txt")
    data = file.readData()
    arr = []
    for i in range(len(data) - 1):
        arr.append(data[i].getCoordinates())
    arr.append(data[len(data) - 1])
    file = FileH.FileHandling("Text/output.txt")
    file.writeData(arr)

