from PIL import Image
import numpy as np
from Coordinate import Coordinate

class Bitmap:
    ############################# Attributes #############################
    __bitmapArray = None

    ############################# Constructor #############################
    def __init__(self, bitmapPath):
        """
        Tham số khởi tạo là đường dẫn của file .bmp
        """
        self.bitmapPath = bitmapPath

    ############################# Methods #############################
    def toArray(self):
        """
        Phương thức này trả về ma trận màu Pixel ở dạng số

        Return:
               arr: ma trận số
        Rtype:
              numpy array
        """
        
        bitmap = Image.open(self.bitmapPath)
        bitmap = bitmap.convert("L")
        self.__bitmapArray = np.asarray(bitmap)
        bitmap.close()

        return self.__bitmapArray

    def getHeight(self) -> int:
        """
        Trả về chiều cao của bitmap
        """
        return len(self.__bitmapArray)
    def getWidth(self) -> int:
        """
        Trả về chiều ngang của bitmap
        """
        return len(self.__bitmapArray[0])
        
    def changeColorOfPixel(self, saveBitmapPath: str, coordinates):
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
            x, y = coordinates[i].x, coordinates[i].y
            bitmap.putpixel((y, x), RGB)

        bitmap.show()
        bitmap.save(saveBitmapPath)
        bitmap.close()
