def main():

    with open('D:\Downloads\codeEnv\ch11\Excercises\studentdata.txt', 'r') as sd:
        
        print('Names\tAverage\n')
        
        for student in sd:
            row = student.split(' ')
            names = row[0]
            grades = row[1:]

            sumGrade = 0
            for grade in grades:
                grade = int(grade)
                sumGrade += grade
                
            average = sumGrade/len(grades)   
            print(f'{names}\t{average:.2f}\n')
    
if __name__ == '__main__':
    main()