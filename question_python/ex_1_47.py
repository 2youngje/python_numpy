math_scores = [40,60,80]
english_scores = [30,40,50]

n_class = 2
n_student = len(math_scores)

score_sum = list()
score_mean = list()

for _ in range(n_class):
    score_sum.append(0)

for student_idx in range(n_student):
    score_sum[0] += math_scores[student_idx]
    score_sum[1] += english_scores[student_idx]

print("sums of scores: ", score_sum)

for class_idx in range(n_class):
    class_mean = score_sum[class_idx]/n_class
    score_mean.append(class_mean)
print("means of scores: ", score_mean)