#분산과 표준편차

scores = [10,20,30]

n_student = len(scores)
score_sum, score_square_sum = 0,0

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum /n_student
square_of_mean = mean **2
mean_of_sqare = score_square_sum / n_student

variance = mean_of_sqare - square_of_mean
std = variance ** 0.5

for student_idx in range(n_student):
    scores[student_idx] = (scores[student_idx]-mean) / std
print(scores)

n_student = len(scores)
score_sum, score_square_sum = 0,0

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum /n_student
square_of_mean = mean **2
mean_of_sqare = score_square_sum / n_student

variance = mean_of_sqare - square_of_mean
std = variance ** 0.5

print("mean: ",mean)
print("standard deviation: ", std)