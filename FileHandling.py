from Coordinates import Coordinates

class FileHandling:

    def __init__(self, filePath):
        self.filePath = filePath

    def readData(self):
        file = open(self.filePath, "r")
        if file:
            _strs = file.readlines()
            
            temp = _strs[0]
            temp = temp.replace("(", "")
            temp = temp.replace(")", "")
            temp = temp.replace("\n", "")
            start = temp.split(";")
            startXY = Coordinates(int(start[0]), int(start[1]))


            temp = _strs[1]
            temp = temp.replace("(", "")
            temp = temp.replace(")", "")
            temp = temp.replace("\n", "")
            goal = temp.split(";")
            goalXY = Coordinates(int(goal[0]), int(goal[1]))
            

            m = int(_strs[2])

            file.close()

            return startXY, goalXY, m

    def writeData(self, arr):
        file = open(self.filePath, "w")
        for data in arr:
            file.write(str(data) + "\n")

        file.close()
