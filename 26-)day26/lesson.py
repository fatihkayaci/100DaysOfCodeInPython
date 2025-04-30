# numbers = [1, 2, 3]
# new_item = [n + 1 for n in numbers]
# print(new_item)



# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)


# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)


# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
# short_names = [name.upper() for name in names if len(name) >= 5]
# print(short_names)

# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# random_number = random.Random()
# students_scores = {student : random_number.randint(1, 100) for student in names}
# print(students_scores)

# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)


import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.score >= 90:
        print(row.student)