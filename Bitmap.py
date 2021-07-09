from os import name
from PIL import Image
import numpy as np

class Bitmap():
    def __init__(self, __bitmapPath):
        self.bitmapPath = __bitmapPath

    def __openBitmap(self):
        bitmap = Image.open(self.bitmapPath)
        bitmapArray = np.asarray(bitmap)
        return bitmapArray
        
    def asArray(self):
        bitmapArray = self.__openBitmap()

        row = len(bitmapArray)
        column = len(bitmapArray[0])
        arr = np.zeros((row, column))
        for i in range(len(bitmapArray)):
            for j in range (len(bitmapArray[0])):
                arr[i][j] = int(bitmapArray[i][j][0])

        return arr



if __name__ == "__main__":
    bitmap = Bitmap("Bitmap/test_case_4x4.bmp")
    print(bitmap.asArray())
