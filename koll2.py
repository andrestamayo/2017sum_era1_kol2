import json

class School(object):
    """docstring for School."""
    def __init__(self):
        super(School, self).__init__()
        self.cont=0
        self.subjects={}

    def create_course(self, subject):
        self.subjects[subject]={}

    def enrroll_student_in_subject(self, subject, student_name, student_surname):
        self.subjects[subject][student_name]=[student_surname,0,[]]

    def add_grade(self,subject,student_name,grade ):
        self.subjects[subject][student_name][2].append(grade)

    def attend(self,subject,student_name):
        self.subjects[subject][student_name][1]+=1

    def get_subject_avg(self, subject):
        sum=0
        for std in self.subjects[subject]:
            sum=sum+self.get_student_avg_grade_in_subject(subject, std)
        return sum/len(self.subjects[subject])

    def get_student_avg_grade_in_subject(self,subjet, student):
        sum=0
        self.cont+=1
        for grade in self.subjects[subjet][student][2]:
            sum= sum+grade
        sum=sum/len(self.subjects[subjet][student][2])
        return sum
    def get_total_students_avg(self):
        sum=0
        for sbjt in self.subjects:
            sum=sum+ self.get_subject_avg(sbjt)
        return sum/len(self.subjects)
    def get_student_avg_in_total(self,student):
        sum=0;
        self.cont=0
        for sbjt in self.subjects:
            sum=sum+self.get_student_avg_grade_in_subject(sbjt,student)
        sum=sum/self.cont
        return sum
    def get_json(self):
        with open('output_file.json','w') as fp:
            json.dump(self.subjects,fp)
    def init_from_json(self):
        with open('output_file.json') as data_file:
            self.subjects=json.load(data_file)
        pass
print('build')
school= School()
school.create_course('python')
school.enrroll_student_in_subject('python','Andrés','tamayo')
school.attend('python','Andrés')
school.add_grade('python','Andrés',10)
school.get_json()
print(school.subjects)
print(school.get_total_students_avg())
print(school.get_student_avg_in_total('Andrés'))
school.subjects={}
school.init_from_json()
print(school.subjects)
