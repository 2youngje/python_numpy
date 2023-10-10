#dir 함수로 list의 속성을 프린트
a = [1,2,3]
for attr in dir(a):
    print(attr)

print('----------------')
#dir 함수로 디렉토리의 속성을 프린트
b = {'a':1}
for dic in dir(b):
    print(dic)