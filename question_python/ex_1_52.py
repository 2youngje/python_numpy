math_scores, english_scores = [50, 60, 70], [30, 40, 50]

''' EX 1-51 start '''
n_student = len(math_scores)

math_sum, english_sum = 0, 0
math_square_sum, english_square_sum = 0, 0

for student_idx in range(n_student):
    # 수학 점수의 합
    math_sum += math_scores[student_idx]
    # 수학 점수 제곱의 합
    math_square_sum += math_scores[student_idx]**2

    # 영어 점수의 합
    english_sum += english_scores[student_idx]
    # 영어점수 제곱의 합
    english_square_sum += english_scores[student_idx]**2

# 수학 평균 = 수학점수 합 / 학생수
math_mean = math_sum / n_student
# 영어 평균 = 영어점수 합 / 학생수
english_mean = english_sum / n_student

# 수학 점수 분산 = 수학 점수 제곱의 합 / 학생수 (빼기 - ) 수학 평균의 제곱
math_variance = math_square_sum/n_student - math_mean**2

# 영어 점수 분산 = 영어 점수 제곱의 합 / 학생수 (빼기 - ) 영어 평균의 제곱
english_variance = english_square_sum/n_student - english_mean**2

# 수학 점수의 표준편차 = 수학 점수의 분산에 제곱근 (**0.5)
math_std = math_variance**0.5

# 영어 점수의 표준편차 = 영어 점수의 분산에 제곱근 (**0.5)
english_std = english_variance**0.5
''' Ex 1-51 end '''

# student_idx가 n_student 만큼 loop 을 돌면서 수행 (실제 리스트 길이 만큼)
for student_idx in range(n_student):
    # x                     :=                     x-μ               /   σ
    math_scores[student_idx] = (math_scores[student_idx] - math_mean)/math_std
    english_scores[student_idx] = (english_scores[student_idx] - english_mean)/english_std

print("Math scores after standardization : ", math_scores)
print("English scores after standardization : ", english_scores)
print("mean/std of math: ", math_mean, math_std)
print("mean/std of english : ", english_mean, english_std)