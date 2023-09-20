#Mean Squared Error
predictions = [10,20,30]
label = [10,25,40]

#predictions의 길이
n_data = len(predictions)
#diff_square_sum의 값을 초기화
diff_square_sum = 0

#data_idx를 설정하고 n_data까지 반복
for data_idx in range(n_data):
#각 라벨의 값의 차이를 구하고 제곱
    diff_square_sum += (predictions[data_idx] - label[data_idx])**2
#제곱한 값을 가지고 n_data를 나눔
mse = diff_square_sum/n_data
print("MSE: ",mse)