grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sum_grades = [sum(grade) for grade in grades]
print(sum_grades)
len_grades = [len(grade) for grade in grades]
print(len_grades)
mid_grades = [a / b for a, b in zip(sum_grades, len_grades)]
print(mid_grades)
students_grades = dict(zip(sorted(students), mid_grades))
print(students_grades)
