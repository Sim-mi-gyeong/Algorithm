import sys

# sys.stdin = open("./test.txt", "r")
input = sys.stdin.readline
from collections import deque


def init(N, M, l):
    global belts, id_belt, id_weight
    belts = {i: deque() for i in range(1, M + 1)}
    ids = [int(next(l)) for _ in range(N)]
    weights = [int(next(l)) for _ in range(N)]
    j = 0
    for i in range(1, M + 1):
        for _ in range(N // M):
            belts[i].append((ids[j], weights[j]))
            id_belt[ids[j]] = i
            id_weight[ids[j]] = (ids[j], weights[j])
            j += 1
    pass


# 물건 하차 + 무게 출력
def forwarding(w_max):
    global belts, id_belt
    s = 0
    for i in belts:
        if not belts[i]:
            continue
        # print(i, " 번 벨트 상태 : ", belts[i])
        if belts[i][0][1] <= w_max:
            r_id, w = belts[i].popleft()
            s += w
            del id_belt[r_id]
        else:
            belts[i].rotate(-1)
    print(s)
    return


# 물건 제거
def erase(r_id):
    global belts, id_belt
    to_return = -1
    if r_id in id_belt:
        to_return = r_id
        b_num = id_belt[r_id]
        target = id_weight[r_id]
        belts[b_num].remove(target)
        del id_weight[r_id]
        del id_belt[r_id]
    print(to_return)
    return


# 물건 확인
def check(f_id):
    global belts
    belt_num = -1
    if f_id in id_belt:
        belt_num = id_belt[f_id]
        # print("찾는 상자가 있는 벨트 : ", belt_num)
        while belts[belt_num][0][0] != f_id:
            belts[belt_num].rotate(-1)

    # print("찾는 상자가 있는 벨트 : ", belt_num)
    print(belt_num)
    return


# 벨트 고장
def broken(b_num):
    global belts, id_belt, broked
    if b_num not in belts:
        b_num = -1
        print(b_num)
        return
    next_belt = b_num + 1 if b_num != len(belts) else 1
    while next_belt in broked:
        next_belt = b_num + 1 if b_num != len(belts) else 1
    broked.add(b_num)
    belts[next_belt].extend(belts[b_num])
    del belts[b_num]
    for r_id, b in id_belt.items():
        if b == b_num:
            id_belt[r_id] = next_belt
    print(b_num)
    return


def solution():
    q = int(input())
    for _ in range(q):
        line = iter(input().split())
        cmd = int(next(line))
        if cmd == 100:
            n, m = int(next(line)), int(next(line))
            init(n, m, line)
        elif cmd == 200:
            w = int(next(line))
            forwarding(w)
        elif cmd == 300:
            erase(int(next(line)))
        elif cmd == 400:
            check(int(next(line)))
        elif cmd == 500:
            broken(int(next(line)))
    return


belts = {}
id_belt = {}
broked = set()
id_weight = {}
solution()
