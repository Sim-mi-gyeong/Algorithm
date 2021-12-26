# 20억 조건 : 정수형 데이터를 위해 기본 int형을 사용할 경우 21억 정도까지 값이 형성될 수 있음.
# -> 최대값 명시 조건(파이썬에서는 무관)
import time
start_time = time.time()

string = input()
max = int(string[0])

for i in range(len(string[:-1])):
    if max + int(string[i+1]) > max * int(string[i+1]):
        max += int(string[i+1])
    else:
        max *= int(string[i+1])

end_time = time.time()
print(max)
print("수행 시간 : ", end_time - start_time)
