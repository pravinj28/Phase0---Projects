

class Student():
    School_name = "FDE Academy"
    student_count = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 
        Student.student_count += 1
    def average(self):
        return sum(self.grade)/len(self.grade)
    
    def is_passing(self):
        return self.average() >= 40

    def add_grade(self, grade):
        self.grade.append(grade)
    
    def __str__(self):
        return f"Student:{self.name}, Average:{self.average():.2f}"


@classmethod

def get_count(cls):
    return f"Total Students: {cls.student_count}"

@staticmethod

def is_valid_frade(grade):
    return 0 <= grade <= 100


s1 = Student("Raj", 20, [85, 90, 78])
s2 = Student("Priya", 21, [92, 88, 95])

print(s1)                   
print(s2)                    
print(s1.is_passing())       
s1.add_grade(95)
print(s1.average())         
print(Student.student_count) 
    
class GraduateStudent(Student):
    def __init__(self, name, age, grade, thesis_topic):
        super().__init__(name, age, grade)
        self.thesis_topic = thesis_topic

        def __str__(self):
            return f"Graduate: {self.name}, Thesis: {self.thesis_topic}"

gs = GraduateStudent("Amit", 24, [88,89], "AI in Healthcare")
print(gs)
print(gs.average())
print(gs.is_passing)



