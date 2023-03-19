from domains.student import Student
from domains.course import Course
import math
import numpy as np

class Output:
    def __init__(self, student_list: list, course_list: list):
        self.student_list: list = student_list
        self.course_list: list = course_list

    def getStudentList(self):
        return self.student_list 
    def getCourseList(self):
        return self.course_list 

    def gpaBoard(self):
        gpa_list: list = []
        for student in self.student_list:
            gpa_list.append(student.s_gpa)
        gpa_list = np.flip(np.sort(np.array(gpa_list)))
        for gpa in gpa_list:
            for student in self.student_list:
                if student.s_gpa == gpa:
                    print("| {:^15} | {:^15} | {:^15} |".format("ID", "Name", "GPA"))
                    print("| {:^15} | {:^15} | {:^15} |".format(student._Student__s_id, student._Student__s_name, student.s_gpa))

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
