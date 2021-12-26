# 문제 해결 아이디어
# 오름차순 정렬 이후 공포도가 가장 낮은 모험가부터 하나씩 확인
# 앞에서부터 공포도를 확인하며, '현재 그룹에 포함된 모험가 수 >= 현재 확인하는 공포도' 이면 그룹 설정
# 공포도가 오름차순 정렬 -> 항상 최소한의 모험가 수만 포함해 그룹 결성
import time
start_time = time.time()

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0   # 총 그룹의 수
count = 0   # 햔재 그룹에 포함된 모험가 수

for i in data:   # 공포도를 낮은 것부터 하나씩 확인
    count += 1   # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:   # 현재 그룹에 포함된 모험가 수 >= 현재 공포도 -> 그룹 O
        result += 1   # 총 그룹 수 + 1
        count = 0   # 현재 그룹에 포함된 모험가 수 초기화

end_time = time.time()
print(result)
print("걸린 시간 : ", end_time - start_time)