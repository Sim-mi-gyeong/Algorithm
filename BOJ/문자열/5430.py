# AC

import re
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    check = True
    func = input()
    n = int(input())
    s = input().strip()
    # lst = re.findall("[0-9]+", s)
    lst = s[1:-1].split(",")
    queue = deque(lst)
    if n == 0:
        queue = deque()

    cnt = 0

    for f in func:
        if f == "R":
            cnt += 1
            # queue.reverse()   # R 이 나올 때마다 reverse() 를 하면 R의 최대 횟수 100,000 , 배열의 최대 크기 100 , 테스트케이스 100개 -> 1억번의 시간 소요
        elif f == "D":
            #  pop(0)을 호출하면 첫 번째 원소를 제거한 후 그 뒤의 원소를 전부 일일이 한 칸씩 앞으로 당김 -> O(N)
            if len(queue) == 0:
                check = False
                print("error")
                break
            else:
                if cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if check:
        if cnt % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
