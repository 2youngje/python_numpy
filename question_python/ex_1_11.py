#ex_1_11 분산의 정의
score1 = 10
score2 = 20
score3 = 30
n_student = 3

mean = (score1+score2+score3)/n_student
square_of_mean = mean**2
mean_of_square = (score1**2 + score2**2 + score3**2)/n_student

print(f"square of mean : {square_of_mean}")

print(f"mean of square : {mean_of_square}")