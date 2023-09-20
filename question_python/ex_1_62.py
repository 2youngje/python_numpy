sec = 5000
min = 0
hour = 0
if sec >= 60:
    hour = sec // 3600
    sec -= hour*3600

    min = sec // 60
    sec -= min*60

else:
    min = 0
print(f'입력한 시간은 {hour}시 {min}분 {sec}초 입니다')