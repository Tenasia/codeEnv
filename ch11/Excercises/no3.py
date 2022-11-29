
def main():
    
    with open('D:\Downloads\codeEnv\ch11\Excercises\studentdata.txt', 'r') as sd:
        
        print('Name\tMIN\tMAX\n')
        for student in sd:
            row = student.split(' ')
            names = row[0]
            grades = row[1:]
        
            min = int(grades[0])
            max = int(grades[0])
            for grade in grades:
                grade = int(grade)
                
                if grade > max:
                    max = grade
                elif grade < min:
                    min = grade
            
            print(f'{names}\t{min}\t{max}\n')

if __name__ == '__main__':
    main()