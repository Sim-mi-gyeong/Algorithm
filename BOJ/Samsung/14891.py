# 톱니바퀴

# 회전시킬 톱니바퀴 / 회전시킬 방향
# 서로 맞닿은 극에 따라서 -> 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있음
# 톱니바퀴 A를 회전 -> 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면 -> B는 A가 회전한 방향과 반대방향으로 회전
# 극이 같으면 회전 X

# 입력
# 톱니바퀴의 초기 상태 / 톱니바퀴를 회전시킨 방법
# 12시방향부터 시계방향 순서대로 - N극은 0, S극은 1로

# k : 회전 횟수
# 회전 방법 - (회전시킨 톱니바퀴 번호,  방향)
# 방향: 1 = 시계 / -1 = 반시계

# 출력
# 최종 톱니바퀴의 상태
# K번 회전시킨 이후에 네 톱니바퀴의 점수의 합

# 점수 : n 번 톱니바퀴의 12시 방향이 N 극이면 0점 / S 극이면 2**(n-1) 점

"""
10101111
01111101
11001110
00000010
2
3 -1
1 1
"""

# 톱니바퀴의 시계방향(1) 회전 : 인덱스 i += 1 / 마지막 -> 0으로
# 0 -> 1  /  7 -> 0 으로
# 톱니바퀴의 반시계방향(-1) 회전 : 인덱스 i -= 1 / 첫번째 -> 마지막으로
# 1 -> 0 / 0 -> 7 로

# 시계 방향 : i = (i + 1) % 8

# 반시계 방향 : i = (i + 7) % 8

# 맞닿은 부분 확인 ->
# (1번의 3번째, 2번의 7번째) / (2번의 3번쨰, 3번의 7번째) / (3번의 3번째, 4번의 7번째)
# 인덱스 기준
# (1번의 2, 2번의 6) / (2번의 2, 3번의 6) / (3번의 2 4번의 6)

from collections import deque

# num1 = list(map(int, input()))
# num2 = list(map(int, input()))
# num3 = list(map(int, input()))
# num4 = list(map(int, input()))
for t in range(4):
    lst = list(map(int, input()))
    q1, q2, q3, q4 = deque(), deque(), deque(), deque()
    for i in range(8):
        if t == 0:
            q1.append(lst[i])
        elif t == 1:
            q2.append(lst[i])
        elif t == 2:
            q3.append(lst[i])
        else:
            q4.append(lst[i])


# num = [num1, num2, num3, num4]
num = [q1, q2, q3, q4]
k = int(input())


def rotation():

    return num


for _ in range(k):
    n, dir = map(int, input().split())  # 회전시킬 번호, 방향
    # 회전시킬 톱니바퀴는 먼저 회전 시켜
    # 인접한 부분끼리 극이 다르면 회전
    # 인접한 부분끼리 극이 같으면 회전X

    # if dir == 1:
    #     for i in range(len(num[n - 1])):
    #         newIdx = (i + 1) % 8
    #         num[n - 1][newIdx] = num[n - 1][i]
    # else:
    #     for i in range(len(num[n - 1])):
    #         newIdx = (i + 7) % 8
    #         num[n - 1][newIdx] = num[n - 1][i]

    # 회전 시킬 톱니바퀴 좌우 먼저 확인
    if num[n - 1][2] != num[n][6]:  # 3번과 4번이 다르면 -> 회전
        # 4번은 3번과 반대로 / 같으면 회전 X
        if dir == 1:  # 시계 방향
            for i in range(len(num[n - 1])):
                newIdx = (i + 1) % 8
                num[n - 1][i], num[n - 1][newIdx] = num[n - 1][newIdx], num[n - 1][i]  # 자리 바꾸기

            for i in range(len(num[n - 1])):  # 얘는 반시계 방향
                newIdx = (i + 7) % 8
                num[n][newIdx] = num[n][i]
                num[n - 1][i], num[n - 1][newIdx] = num[n - 1][newIdx], num[n - 1][i]

        else:  # 반시계 방향
            for i in range(len(num[n - 1])):
                newIdx = (i + 7) % 8
                num[n - 1][newIdx] = num[n - 1][i]
                num[n - 1][i], num[n - 1][newIdx] = num[n - 1][newIdx], num[n - 1][i]

            for i in range(len(num[n - 1])):  # 3번은 시계 방향
                newIdx = (i + 1) % 8
                num[n][newIdx] = num[n][i]
                num[n - 1][i], num[n - 1][newIdx] = num[n - 1][newIdx], num[n - 1][i]

    print(num)

    # 3번과 2번이 다르면 -> 반대 , 같으면 회전 X
    # if num[n - 1][6] != num[n - 1][2]:
    #     if dir == 1:
    #         for i in range(len(num[n - 1])):
    #             newIdx = (i + 1) % 8
    #             num[n - 1][newIdx] = num[n - 1][i]
    #     else:
    #         for i in range(len(num[n - 1])):
    #             newIdx = (i + 7) % 8
    #             num[n - 1][newIdx] = num[n - 1][i]
