#ex_1_12 분산과 표준편차
score1 = 10
score2 = 20
score3 = 30
n_student = 3

mean = (score1+score2+score3)/n_student
square_of_mean = mean**2
mean_of_square = (score1**2 + score2**2 + score3**2)/n_student


score_variance = mean_of_square - square_of_mean
score_std = score_variance ** 0.5

print(f"mean : {mean}")

print(f"variance : {score_variance}")

print(f"standard deviation : {score_std}")