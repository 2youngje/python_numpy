#성적을 평점으로 바꾸기
scores = [20,50,10,60,70]
grades = list()

for score in scores:
    if score >80:
        grades.append('A')
    elif score >60:
        grades.append('B')
    elif score >40:
        grades.append('C')
    else:
        grades.append('F')

print(grades)