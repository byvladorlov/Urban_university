grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score = dict()
a = float(sum(grades[0])/len(grades[0]))
b = float(sum(grades[1])/len(grades[1]))
c = float(sum(grades[2])/len(grades[2]))
d = float(sum(grades[3])/len(grades[3]))
e = float(sum(grades[4])/len(grades[4]))
sort_students = sorted(students)
average_score.update(({sort_students[0]: a, sort_students[1]: b, sort_students[2]: c, sort_students[3]: d, sort_students[4]: e}))
print(average_score)