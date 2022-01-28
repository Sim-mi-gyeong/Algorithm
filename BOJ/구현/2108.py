# 통계학

import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
# 산술평균 - 소수점 이하 첫째 자리에서 반올림한 값
print(sum(num) // len(num))
# 중앙값
print(num[int(len(num) / 2)])

# 최빈값 - 여러 개 있을 경우 최빈값 중 두 번째로 작은 값
# value = {}
# small = []
# cnt = 0
# for i in num:
#     value[i] = 0
# for i in num:
#     if i in value.keys():
#         value[i] += 1
# for j in value.values():
#     if cnt < j:
#         cnt = j
# for i, j in value.items():
#     if j == cnt:
#         small.append(i)

# print(small[1])
from scipy.stats import mode
print(mode(num))

# 범위 출력
print(max(num) - min(num))
