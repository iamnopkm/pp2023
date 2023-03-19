class Student:
    def __init__(self, s_id: str, s_name: str, s_DoB: str, gpa: float):
        self.__s_id = s_id
        self.__s_name = s_name
        self.__s_DoB = s_DoB
        self.s_gpa = gpa
        
       
    def getS_id(self):
        return self.__s_id
    def getS_name(self):
        return self.__s_name
    def getS_DoB(self):
        return self.__s_DoB
    def getS_gpa(self):
        return self.s_gpa
    
    
    def setS_id(self, s_id: str):
        self.__s_id = s_id
    def setS_name(self, s_name: str):
        self.__s_name = s_name
    def setS_DoB(self, s_DoB: str):
        self.__s_DoB = s_DoB
    def getS_gpa(self, gpa: float):
        self.s_gpa = gpa