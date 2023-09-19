scores = [10,20,30]

#method.1
score_sum = 0
n_student = 0
for score in scores:
    score_sum += score
    n_student += 1
score_mean = score_sum / n_student
print("score mean : ",score_mean)

scores_ms = list()
for score in scores:
    scores_ms.append(score - score_mean)
print(scores_ms)

#method.2
score_sum = 0
n_student = 0
for score in scores:
    score_sum += score
    n_student += 1
score_mean = score_sum / n_student
print("score mean : ",score_mean)

for score_idx in range(len(scores)):
    scores[score_idx] -= score_mean
print(scores)