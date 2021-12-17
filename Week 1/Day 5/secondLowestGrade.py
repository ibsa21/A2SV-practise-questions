if __name__ == '__main__':
    students = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        grades.append(score)
    
    
    minGrade  = min(grades)
    secondGrade = grades
    for i in range(secondGrade.count(minGrade)):
        secondGrade.remove(minGrade)
        
    secondMinGrade = min(secondGrade)
    students.sort()
    for i in range(len(students)):
        if(students[i][1]==secondMinGrade):
            print(students[i][0])
    
