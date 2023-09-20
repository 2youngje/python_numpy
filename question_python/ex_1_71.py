#n배수들의 합 구하기

mltiple_of = 3

numbers = list()
for num in range(100):
    numbers.append(num)

sum_multiple_of_n = 0
for num in numbers:
    if num % mltiple_of == 0:
        sum_multiple_of_n += num
print(sum_multiple_of_n)