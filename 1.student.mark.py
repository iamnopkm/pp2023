"""New version"""
def courseList() -> dict:
    c_list: dict = {"ID": [], "Name": []}
    number_of_course: int = getCourseNumber()
    for course in range(number_of_course):
        c_id, c_name = getCourseInfo()
        c_list["ID"].append(c_id)
        c_list["Name"].append(c_name)
        print(f"Course with ({c_id}: {c_name}) has created")
    print("\nList of current course:", c_list)
    return c_list
    
def studentList() -> dict:
    s_list: dict = {"ID": [], "Name": [], "Date of birth": []}   
    number_of_student: int = getStudentNumber()
    for student in range(number_of_student):
        s_id, s_name, s_DoB = getStudentInfo()
        s_list["ID"].append(s_id)
        s_list["Name"].append(s_name)
        s_list["Date of birth"].append(s_DoB)
        print(f"Student {s_name} id {s_id}  has join the battle")     
    print("\nList of enrolled student:", s_list)
    return s_list

def getStudentNumber() -> int:
    number_of_student: int = int(input("\nEnter number of student in the class: "))
    return number_of_student

def getStudentInfo() -> str:
    s_id: str = input("\nEnter student id (EX: BI12-xxx): ")
    s_name: str = input("\nEnter student name: ")
    s_DoB: str = input("\nEnter student date of birth (EX: 30-07-2003): ")
    return s_id, s_name, s_DoB

def getCourseNumber() -> int:
    number_of_course: int = int(input("\nEnter number of course: "))
    return number_of_course

def getCourseInfo() -> str:
    c_id: str = input("\nEnter course id: ")
    c_name: str = input("\nEnter course name: ")
    return c_id, c_name

def getMark(): 
    s_list: dict = studentList()
    c_list: dict = courseList()
    ask_c_id: str = input("\nWhich course do you choose: ")
    final_dict: dict = {"Student ID": [], "Mark": []}
    
    if ask_c_id in c_list["ID"]:
        print("\nThe course does exsist!!!")
        promp = int(input("\nHow many student in this course: "))
        if promp <= len(s_list["ID"]):
            for student in range(promp):
                ask_s_id: str = input("\nChoose student id: ")
                if ask_s_id in s_list["ID"]:
                    get_mark = input(f"\nEnter mark for student {ask_s_id}: ")
                    final_dict["Student ID"].append(ask_s_id)
                    final_dict["Mark"].append(get_mark)
                  
             
            print("\nIn the course id " + ask_c_id + ":")
            print(final_dict) 
           
    
        else:
            print("\nSomething wrong with the number of student")
        
                
                        
                    

                
    
    
mark = getMark()



         

"""Old version"""
# def printList(l1):
#     x = 0
#     y = 0
#     for element1 in l1:
#         while x < len(l1[0]) and y < len(l1[1]):
#             print("Student id " + l1[0][x] + " has the mark: " + l1[1][y])
#             x += 1
#             y += 1

# def courseList() -> list:
#     c_list: list = []
#     number_of_course: int = getCourseNumber()
#     for course in range(number_of_course):
#         c_id, c_name = getCourseInfo()
#         c_list.append((c_id, c_name))
#         print(f"Course with ({c_id}: {c_name}) has created")
#     print("\nList of current course:", c_list)
#     return c_list
    
# def studentList() -> list:
#     s_list: list = []    
#     number_of_student: int = getStudentNumber()
#     for student in range(number_of_student):
#         s_id, s_name, s_DoB = getStudentInfo()
#         s_list.append((s_id, s_name, s_DoB))
#         print(f"Student {s_id} has join the battle")     
#     print("\nList of enrolled student:", s_list)
#     return s_list

# def getStudentNumber() -> int:
#     number_of_student: int = int(input("\nEnter number of student in the class: "))
#     return number_of_student

# def getStudentInfo() -> str:
#     s_id: str = input("\nEnter student id (EX: BI12-xxx): ")
#     s_name: str = input("\nEnter student name: ")
#     s_DoB: str = input("\nEnter student date of birth (EX: 30-07-2003): ")
#     return s_id, s_name, s_DoB

# def getCourseNumber() -> int:
#     number_of_course: int = int(input("\nEnter number of course: "))
#     return number_of_course

# def getCourseInfo() -> str:
#     c_id: str = input("\nEnter course id: ")
#     c_name: str = input("\nEnter course name: ")
#     return c_id, c_name

# def getMark(): 
#     mark_list: list = []
#     student_list: list = []
#     c_list = courseList()
#     s_list = studentList()
#     ask_c_id: str = input("\nWhich course do you choose: ")
#     combine_list = [student_list, mark_list]
    
#     if ask_c_id in (item for sublist in c_list for item in sublist):
#         print("\nThe course does exsist!!!")
#         promp = int(input("\nHow many student in this course: "))
#         if promp <= len(s_list):
#             for student in range(promp):
#                 ask_s_id: str = input("\nChoose student id: ")
#                 if ask_s_id in (item for sublist in s_list for item in sublist):
#                     get_mark = input(f"\nEnter mark for student {ask_s_id}: ")
#                     mark_list.append(get_mark)
#                     student_list.append(ask_s_id)
                    
#             print(combine_list)
#             print("\nIn the course id " + ask_c_id + ":")
#             printList(combine_list)
    
#         else:
#             print("\nSomething wrong with the number of student")
        
                
                        
                    

                
    
    
# mark = getMark()

         