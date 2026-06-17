import csv

def read_students(filename):
    students = []
    with open( filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students
    
data = read_students("students.csv")
print(data)

def calculate_averages(students):
    student_marks = {}

    for row in students:
        name = row["name"]
        marks = int(row["marks"])
        if name in student_marks:
            student_marks[name].append(marks)
        else:
            student_marks[name] = [marks]
        
    averages = {}
    for name in student_marks:
        marks_list = student_marks[name]
        averages[name] = sum(marks_list) / len(marks_list)
    return averages

averages = calculate_averages(data)
print(averages)

def rank_students(averages):
    pairs =list(averages.items())
    ranked = sorted(pairs, key = lambda x: x[1], reverse= True)
    return ranked

ranked = rank_students(averages)
print(ranked)

def find_topper_per_subject(students):
    subject_data = {}

    for row in students:
        subject = row["subject"]
        name = row["name"]
        marks = int(row["marks"])
        if subject in subject_data:
            subject_data[subject].append((name, marks))
        else:
            subject_data[subject] = [(name, marks)]
    
    toppers = {}
    for subject in subject_data:
        pairs = subject_data[subject]
        highest = max(pairs, key = lambda x: x[1])
        toppers[subject] = highest

    return toppers

toppers = find_topper_per_subject(data)
print(toppers)

def write_summary(ranked, toppers, filename):
    with open(filename, "w", newline= "") as file: 
        headers = ["rank", "name", "average", "topper_in_subject"]
        writer = csv.DictWriter(file, fieldnames= headers)
        writer.writeheader()

        for rank, (name, averages) in enumerate(ranked, start=1):
            topped_subject = "None"
            for subject, (topper_name, topper_marks) in toppers.items():
                if topper_name == name:
                    topped_subject = subject
    
            writer.writerow({
            'rank': rank,
            'name': name,
            'average': averages,
            'topper_in_subject': topped_subject
            })
                   
write_summary(ranked, toppers, "summary.csv")
print("Done — check summary.csv")

