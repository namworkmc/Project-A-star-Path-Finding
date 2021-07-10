from Coordinate import Coordinate

class FileHandling:

    ############################# Constructor #############################
    def __init__(self, filePath):
        """
        Tham số khởi tạo là đường dẫn của file .txt
        """
        self.filePath = filePath

    ############################# Methods #############################
    def readData(self):
        """
        Phương thức này trả về toạ độ Start, Goal và tham số m

        Returns:
                startXY: toạ độ Start
                goalXY: toạ độ Goal
                m: tham số m

        Rtypes: Coordinate, int
        """
        
        file = open(self.filePath, "r")
        if file:
            # đọc toàn bộ data trong .txt #
            _strs = file.readlines()
            
            # toạ độ Start #
            temp = _strs[0]
            # TODO: làm sạch dữ liệu #
            temp = temp.replace("(", "")
            temp = temp.replace(")", "")
            temp = temp.replace("\n", "")
            start = temp.split(";")
            startXY = Coordinate(int(start[0]), int(start[1]))


            # toạ độ Goal #
            temp = _strs[1]
            # TODO: làm sạch dữ liệu #
            temp = temp.replace("(", "")
            temp = temp.replace(")", "")
            temp = temp.replace("\n", "")
            goal = temp.split(";")
            goalXY = Coordinate(int(goal[0]), int(goal[1]))
            

            # tham số m #
            m = int(_strs[2])

            file.close()

            return startXY, goalXY, m

    def writeData(self, arr):
        """
        Input của phường writeData là một mảng
        """

        file = open(self.filePath, "w")
        for data in arr:
            file.write(str(data) + "\n")

        file.close()
