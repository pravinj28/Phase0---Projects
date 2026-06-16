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

s1 = Student("Raj", 20, [85, 90, 78])
s2 = Student("Priya", 21, [92, 88, 95])

print(s1)                    # should print formatted string
print(s2)                    # should print formatted string
print(s1.is_passing())       # should print True
s1.add_grade(95)
print(s1.average())          # should print new average after adding 95
print(Student.student_count) # should print 2
    


        



