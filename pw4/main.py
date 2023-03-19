from domains.course import Course
from domains.student import Student
from input import Input
from output import Output
import math

class Functionalities:
    def __init__(self):
        self.student_list: list = []
        self.course_list: list = []
        self.input_func = Input(self.student_list, self.course_list)
        self.output_func = Output(self.student_list, self.course_list)
    def run_func(self, option: int):
        match option:
            case 1:
                self.input_func.studentsInfo()
            case 2:
                self.input_func.coursesInfo()
            case 3:
                self.input_func.marksInfo()
            case 4:
                self.output_func.markBoard()
            case 5:
                self.input_func.gpaCalculator()
            case 6:
                self.output_func.gpaBoard()
            case default:
                return "Not correct option"

if __name__ == "__main__":
    flag = Functionalities()
    while True:
        print(f'''Choose an action:
                1.Take student info
                2.Take course info
                3.Mark info
                4.Mark list
                5.GPA calculator
                6.GPA ranking
                ''')
        option: int = int(input("Option: "))
        flag.run_func(option)