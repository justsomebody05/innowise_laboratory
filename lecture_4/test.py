import sqlite3

connection = sqlite3.connect('lecture_4/school.db')
cursor = connection.cursor()

# I'll not check the first 2 querries, because i've made them in main.py file. Checking third querry

cursor.execute('''
SELECT s.full_name, g.subject, g.grade FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';
''')

results = cursor.fetchall()
print("All Alice Johnson's grades:")
for row in results:
    print(f"Student: {row[0]}, Subject: {row[1]}, Grade: {row[2]}") # Good, it's working
print()
    
# checking 4th querry

cursor.execute('''SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC;''')

results1 = cursor.fetchall()
for row in results1:
    print(f"Student: {row[0]}, Average grade: {row[1]:.0f}") # Good, it's working
print()

# cheking 5th querry

cursor.execute('''SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year;''')
results2 = cursor.fetchall()
for row in results2:
    print(f"Student: {row[0]}, Birth year: {row[1]}") # Good, it's working
print()

# checking 6th querry

cursor.execute('''SELECT subject, ROUND(AVG(grade), 2) as average_grade
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;''')
results3 = cursor.fetchall()
for row in results3:
    print(f"Subject: {row[0]}, Average grade: {row[1]}") # Good, it's working
print()

# checking 7th querry

cursor.execute('''SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;''')

results4 = cursor.fetchall()
for row in results4:
    print(f"Subject: {row[0]}, Average grade: {row[1]}") # Good, it's working
print()

# last querry

cursor.execute('''SELECT DISTINCT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name, g.grade;''')

results5 = cursor.fetchall()
for row in results5:
    print(f"Student: {row[0]}, Subject: {row[1]}, Grade: {row[2]}") # good, it's working

connection.commit()
connection.close()