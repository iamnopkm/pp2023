import math
import numpy as np

class Student:
    def __init__(self, s_id: str, s_name: str, s_DoB: str, gpa: float):
        self.__s_id = s_id
        self.__s_name = s_name
        self.__s_DoB = s_DoB
        self.s_gpa = gpa


class Course:
    def __init__(self, c_id: str, c_name: str, c_credit: int):
        self.__c_id = c_id
        self.__c_name = c_name
        self.c_credit = c_credit
        self.mark_sheet = {}

    def getMark(self, s_id: str, mark: float):
        self.mark_sheet[s_id] = mark


class Functionalities:
    def __init__(self):
        self.student_list: list = []
        self.course_list: list = []


    def studentsInfo(self):
        count_student_number: int = int(input("Enter number of student to take info: "))
        if count_student_number > 0:
            print("\nEnter info for students")
            for student in range(count_student_number):
                s_id: str = input("\nEnter student's id: ")
                if s_id not in self.student_list:
                    s_name: str = input("Enter student's name: ")
                    s_date: str = input("Enter student's date birth: ")
                    s_month: str = input("Enter student's month birth: ")
                    s_year: str = input("Enter student's year birth: ")
                    s_Dob_list: list = [s_date, s_month, s_year]
                    s_Dob = "/".join(s_Dob_list)
                    s_gpa: float = 0
                    s_info = Student(s_id, s_name, s_Dob, s_gpa)
                    self.student_list.append(s_info)
                    print(f"{s_id}: {s_name}> Has join the battle")
                else:
                    print("This id already exist pls, re-enter id")
        else:
            print("Invalid number")
        

    def coursesInfo(self):
        count_course_number: int = int(input("Enter number of course: "))
        if count_course_number > 0:
            print(f"\nEnter info for courses")
            for course in range(count_course_number):
                c_id: str = input("\nEnter course's id: ")
                if c_id not in self.course_list:
                    c_name: str = input("Enter course's name: ")
                    c_credit: int = int(input("Enter course's credit: "))
                    c_info = Course(c_id, c_name, c_credit)
                    self.course_list.append(c_info)
                    print(f"Course {c_id}: {c_name} added")
                    for student in self.student_list:
                        c_info.getMark(student._Student__s_id, 0)
                else:
                    print("Course id already exist, pls re-enter")
        else:
            print("Invalid number")

        
    def marksInfo(self):
        print("Enter mark info:")
        for course in self.course_list:
            print(f"{course._Course__c_id}. {course._Course__c_name}")
        ask_c_id: str = str(input("Course's ID: "))
        number_student: int = int(input("Number of students: "))
        if 1 <= number_student <= len(self.student_list):
            for num in range(0, number_student):
                s_id: str = str(input("\nStudent ID: "))
                mark: float = float(input("Mark: "))
                for course in self.course_list:
                    if course._Course__c_id == ask_c_id:
                        course.getMark(s_id, mark)
                        print(f"Mark added for student ID {s_id} in course ID {ask_c_id}.")

        else:
            print("\nInvalid number of students.\n")

    def gpaCalculator(self):
        for student in self.student_list:
            sum_mark: float = 0
            sum_credit: int = 0
            for course in self.course_list:
                if course.mark_sheet[student._Student__s_id]:
                    sum_mark += course.mark_sheet[student._Student__s_id] * course.c_credit
                    sum_credit += course.c_credit
            if sum_credit != 0:
                student.s_gpa = math.floor(sum_mark/sum_credit)
            else:
                student.s_gpa = 0
        print("GPA calculated")
                
    def gpaBoard(self):
        gpa_list: list = []
        for student in self.student_list:
            gpa_list.append(student.s_gpa)
        gpa_list = np.flip(np.sort(np.array(gpa_list)))
        for gpa in gpa_list:
            for student in self.student_list:
                if student.s_gpa == gpa:
                    print(f"Student's ID: {student._Student__s_id}, Student's name: {student._Student__s_name}, GPA: {student.s_gpa}")

    def markBoard(self):
        print("Choose a course:")
        for course in self.course_list:
            print(f"{course._Course__c_id}. {course._Course__c_name}")
        ask_c_id: str = str(input("Which course: "))
        for course in self.course_list:
            if course._Course__c_id == ask_c_id:
                print(f"\nID: {course._Course__c_id}: {course._Course__c_name}")
                print(f"\nReport for {course._Course__c_name}:")
                print("| {:^15} | {:^15} | {:^20} | {:^15} |".format("ID", "Name", "Date of Birth", "Mark"))
                for student in self.student_list:
                    mark = course.mark_sheet[student._Student__s_id]
                    print("| {:^15} | {:^15} | {:^20} | {:^15}|".format(student._Student__s_id, student._Student__s_name, student._Student__s_DoB, mark))
                return
        print(f"Course ID {ask_c_id} not found.")


    def run_func(self, option: int):
        match option:
            case 1:
                Functionalities.studentsInfo(self)
            case 2:
                Functionalities.coursesInfo(self)
            case 3:
                Functionalities.marksInfo(self)
            case 4:
                Functionalities.markBoard(self)
            case 5:
                Functionalities.gpaCalculator(self)
            case 6:
                Functionalities.gpaBoard(self)
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