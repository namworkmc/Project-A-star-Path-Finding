from PIL import Image
import numpy as np

class Bitmap:
    def __init__(self, bitmapPath):
        """
        Tham số khởi tạo là đường dẫn của file .bmp
        """
        self.bitmapPath = bitmapPath

    def __openBitmap(self):
        bitmap = Image.open(self.bitmapPath)
        bitmapArray = np.asarray(bitmap)
        return bitmapArray
        
    def toArray(self):
        """
        Phương thức này trả về ma trận màu Pixel

        Return:
               arr: ma trận số
        Rtype:
              numpy array
        """

        bitmapArray = self.__openBitmap()

        row = len(bitmapArray)
        column = len(bitmapArray[0])
        arr = np.zeros((row, column))
        
        for i in range(len(bitmapArray)):
            for j in range (len(bitmapArray[0])):
                arr[i][j] = int(bitmapArray[i][j][0])

        return arr
