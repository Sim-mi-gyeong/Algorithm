# 문제 해결 아이디어
# 대부분, + 보다는 x 가 더 값을 크게 만듦
# 다만, 두 수 중에서 하나라도 0 혹은 1인 경우 곱하기 보다 < 더하기 수행이 더 효율적
# -> 두 수의 연산 수행 시 두 수 중 하나라도 1 이하인 경우 더하고, 두 수가 모두 2 이상인 경우 곱하기
import time
start_time = time.time()
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1 -> 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

end_time = time.time()
print(result)
print("수행 시간 : ", end_time - start_time)