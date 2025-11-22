students = []

def add_student():
    name = input('Enter students name: ').strip()
    for student in students:
        if student['name'].lower() == name.lower():
            print(f'This student already exist!')
            return 
    students.append({'name': name, 'grades': []})
    
def add_grate():
    name = input('Enter students name: ').strip()
    for student in students:
        if student['name'].lower() == name.lower():
            while True:
                students_grade = input("Enter a grade (or 'done' to finish): ").strip()
                if students_grade.lower() == 'done':
                    break
                try:
                    grade = int(students_grade)
                    if grade >= 0 and grade <= 100:
                        student['grades'].append(grade)
                    else:
                        print('Grade must be between 0 and 100!')
                except ValueError:
                    print('Invalid input. Please, enter a number.')
            return
    print('not found :(')
    
def show_report():
    print('--- Student Report ---')
    total_sum = 0
    total_count = 0
    min_avg = None
    max_avg = None
    for student in students:
        grades = student['grades']
        try:
            average = sum(grades)/len(grades)     
            print(f"{student['name']}'s average grade is {average}")  
            total_sum += average
            total_count += 1
            max_avg = average if max_avg is None else max(max_avg, average)
            min_avg = average if min_avg is None else min(min_avg, average) 
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")
    if total_count > 0:
        overall_average = total_sum/total_count
        print(f'Max average: {max_avg}')
        print(f'Min average: {min_avg}')
        print(f'Overall average: {overall_average}')
    else:
        print(f"Overall average can't be reported")

def top_performer():
    try:
        top_student = max(
            (s for s in students if s["grades"]),key=lambda s: sum(s["grades"]) / len(s["grades"]))
        top_avg = sum(top_student["grades"]) / len(top_student["grades"])
        print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg}.")
    except ValueError:
        print("No top performer found. No students or grades available.")
        
def main():
    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit application")
        
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                add_student()
            elif choice == 2:
                add_grate()
            elif choice == 3:
                show_report()
            elif choice == 4:
                top_performer()
            elif choice == 5:
                print(f'Exiting program.')
                break
            else:
                print('Wrong number. Enter a number from 1 to 5.')
        except ValueError:
            print(f'Invalid input! Enter a number please.')

if __name__ == "__main__":
    main()
        
                        
