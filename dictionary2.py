student = {'name':'nkem', 'school':'unben','grade':(34,56,67,89)}

def average(data):
    grades = data['grade']
    print( sum(grades)/len(grades))

average(student)

def average_grade_all_student(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grade'])
    print(total/count)
average_grade_all_student(student)
