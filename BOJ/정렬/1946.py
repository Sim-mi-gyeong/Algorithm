# 신입 사원
# 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중
# 적어도 하나가 다른 지원자보다 떨어지지 않는 자
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())  # 서류, 면접 순위 각각
        lst.append((a, b))
    lst.sort(key=lambda x: (x[0], x[1]))
    print(lst)
    cnt = 0
    maxCnt = 0
