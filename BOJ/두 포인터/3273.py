# 두 수의 합
# tmpSum = lst[start] == target 인 경우? 
# -> lst[end]를 더하는 단계를 거쳐야 함.
# 시간초과 -> pypy3 / 이분탐색
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
target = int(input())
lst.sort()
cnt = 0

for start in range(n):
    end = start + 1
    tmpSum = lst[start]
    while end < n:
        tmpSum += lst[end]
        if tmpSum == target:
            cnt += 1
            break
        elif tmpSum > target:
            break
        else:
            tmpSum -= lst[end]
            end += 1
print(cnt)
'''
[입력 예시]
6
2 19 41 45 55 58
64
[출력 예시]
1

[입력 예시]
1
2
4
[출력 예시]
0

[입력 예시]
5
1 2 3 4 5
6
[출력 예시]
2
'''