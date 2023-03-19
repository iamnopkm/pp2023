from domains.course import Course
from domains.student import Student
import math

class Input:
    def __init__(self, student_list: list, course_list: list):
        self.student_list: list = student_list
        self.course_list: list = course_list

    def setStudentList(self, student_list: list):
        self.student_list = student_list
    def setCourseList(self, course_list: list):
        self.course_list = course_list

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
                        c_info.setMark(student._Student__s_id, 0)
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
        for num in range(number_student):
            s_id: str = str(input("\nStudent ID: "))
            mark: float = float(input("Mark: "))
            for course in self.course_list:
                if course._Course__c_id == ask_c_id:
                    course.setMark(s_id, mark)
                    print(f"Mark added for student ID {s_id} in course ID {ask_c_id}.")

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