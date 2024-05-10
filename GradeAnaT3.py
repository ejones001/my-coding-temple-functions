def calculate_average_grade (grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

def find_highest_and_lowest_grades(grades):
    if not grades:
        return None, None
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade

def categorize_grades(grades):
    if not grades:
        return None
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    return letter_grades

grades = [85, 92, 78, 90, 65, 88, 72]

# Task 1: Calculate average grade
average_grade = calculate_average_grade(grades)
print("Average grade:", (average_grade)

# Task 2: Find highest and lowest grade
highest_grade, lowest_grade = find_highest_and_lowest_grades(grades)
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)

# Task 3: Categorize grades into letter grades
letter_grades = categorize_grades(grades)
print("Letter grades:", letter_grades)
