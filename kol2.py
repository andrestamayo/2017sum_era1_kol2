#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class School():
    """docstring for School."""
    def __init__(self, school_name, classes):
        
        self.arg = arg
        self.school_name=school_name
        self.classes= classes
    def getStudent_Average(self, arg):
        classes_avg_sumathory=0
        for course in self.classes:
            classes_avg_sumathory=classes_avg_sumathory + course.get_class_average()
        

class Class(object):
    """docstring for Class."""
    def __init__(self, class_name, students):
        
        self.arg = class_name
        self.students = stundents
    def get_class_average(self):

        grade_sumathory=0
        for student in self.students:

            grade_sumathory=grade_sumathory+student.grade
        result= grade_sumathory/ len(self.students)    
        return result
        
class Student(object):
    """docstring for Student."""
    def __init__(self, name, surname, grade):
        self.name=name
        self.surname=surname
        self.grade=grade
        self.attendance=0
        self.arg = arg

    def attent(self, arg):
        self.attendance=self.attendance+1;
        

st9= student('juan', 'martinez', 5)
st8= student('juan', 'martinez', 5)
st7= student('juan', 'martinez', 5)
st6= student('juan', 'martinez', 5)
st5= student('juan', 'martinez', 5)
st4= student('juan', 'martinez', 5)
st2= student('juan', 'martinez', 5)
st3= student('juan', 'martinez', 5)
st1= student('juan', 'martinez', 5)

cl1= Class('Computers', [st1,st2])
cl2= Class('Computers', [st3,st4])
cl3= Class('Computers', [st5,st6])

agh= School('agh', [cl1,cl2,cl3])


        
