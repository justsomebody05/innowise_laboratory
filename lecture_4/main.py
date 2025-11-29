import sqlite3

connection = sqlite3.connect('school.db')
# we using cursor for database manipulation
cursor = connection.cursor()
# here we creating tables
cursor.execute('''CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL)
''')

cursor.execute('''CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL, 
    subject TEXT NOT NULL, 
    grade INTEGER NOT NULL CHECK(grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
)              
''')
# in here we making 2 lists of tuples where we can see a student's info and inserting into our database 
students = [
    ('Alice Johnson', 2005), ('Brian Smith', 2004), ('Carla Reyes', 2006),
    ('Daniel Kim', 2005), ('Eva Thompson', 2003), ('Felix Nguyen', 2007),
    ('Grace Patel', 2005), ('Henry Lopez', 2004), ('Isabella Martinez', 2006)
]
cursor.executemany('INSERT INTO students (full_name, birth_year) VALUES (?, ?)', students)

grades = [
    (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85), 
    (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
    (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
    (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
    (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
    (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
    (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
    (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
    (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92)
]
cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', grades)

connection.commit() # saving all changes
connection.close() # closing our connection