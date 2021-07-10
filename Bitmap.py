from typing import Sequence
from PIL import Image
import numpy as np
from Coordinate import Coordinate

class Bitmap:
    def __init__(self, bitmapPath):
        """
        Tham số khởi tạo là đường dẫn của file .bmp
        """
        self.bitmapPath = bitmapPath

    def __openBitmap(self):
        bitmap = Image.open(self.bitmapPath)
        bitmapArray = np.asarray(bitmap)
        bitmap.close()

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

    def changeColorOfPixel(self, saveBitmapPath: str, coordinates: Coordinate):
        """
        Đổi màu từng pixel dựa trên coordinate
        Param:
                saveBitmapPath: vị trí và tên file lưu
                coordinates: list toạ độ x, y
        """
        bitmap = Image.open(self.bitmapPath)

        # Khởi tạo màu: cam #
        RGB = (250, 130, 45)

        for i in range(len(coordinates)):
            x, y = coordinates[i].getCoordinate()
            bitmap.putpixel((x, y), RGB)

        bitmap.save(saveBitmapPath)
