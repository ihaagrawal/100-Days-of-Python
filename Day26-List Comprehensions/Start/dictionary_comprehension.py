import random

names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
student_scores={student:random.randint(1,101) for student in names}
print(student_scores)

passed_students={student:marks for (student,marks) in student_scores.items() if marks>=60}
print(passed_students)