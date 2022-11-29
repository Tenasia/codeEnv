

import random

def grader(mark):

    print(mark)
    
    marked_grade = []

    if mark >= 90:
        marked_grade.append('A')
    elif mark >= 80:
        marked_grade.append('B')
    elif mark >= 70:
        marked_grade.append('C')
    elif mark >= 60:
        marked_grade.append('D')
    elif mark < 60:
        marked_grade.append('F')

    return marked_grade

def randomGrades():

    grade = []
    for _ in range(10):
        grade.append(int(random.uniform(50, 100)))
    
    return grade

def main():

    values = randomGrades()


if __name__ == '__main__':
    main()