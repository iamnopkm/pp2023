class Course:
    def __init__(self, c_id: str, c_name: str, c_credit: int):
        self.__c_id = c_id
        self.__c_name = c_name
        self.c_credit = c_credit
        self.mark_sheet = {}

    def setC_id(self, c_id: str):
        self.__c_id = c_id
    def setC_name(self, c_name: str):
        self.__c_name = c_name
    def setC_credit(self, c_credit: int):
        self.c_credit = c_credit
    def setMark(self, s_id: str, mark: float):
        self.mark_sheet[s_id] = mark
        
    def getC_id(self):
        return self.__c_id
    def getC_name(self):
        return self.__c_name
    def getC_credit(self):
        return self.c_credit   
    def getMark(self):
        return self.mark_sheet