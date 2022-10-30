from collections import deque
import sys

input = sys.stdin.readline

# 벨트 고장
def cmd_500(b_num):
    global belts, id_belts, belts_status, broken_belts
    if b_num in broken_belts:
        print(-1)
        return

    next_belt = b_num + 1 if b_num != len(belts) else 1
    while next_belt in broken_belts:
        next_belt = b_num + 1 if b_num != len(belts) else 1

    broken_belts.add(b_num)
    if not belts[b_num]:
        del belts[b_num]
        return

    belts[next_belt].extend(belts[b_num])
    del belts[b_num]

    for box_id, box_belt in id_belts.items():
        if box_belt == b_num:
            id_belts[box_id] = next_belt

    print(b_num)
    return


# 물건 확인
def cmd_400(id):
    global belts, id_belts
    target_b_num = -1
    if id in id_belts:
        target_b_num = id_belts[id]
        while belts[target_b_num][0][0] != id:
            # belts[target_b_num].appendleft(belts[target_b_num].pop())
            belts[target_b_num].rotate(-1)

    print(target_b_num)
    return


# 물건 제거
def cmd_300(id):
    global belts, id_belts, id_weight
    return_num = -1
    if id in id_belts:
        return_num = id
        b_num = id_belts[id]
        remove_box = id_weight[id]
        belts[b_num].remove(remove_box)
        del id_belts[id]
        del id_weight[id]

    print(return_num)
    return


# 물건 하차
def cmd_200(w):
    global belts, id_belts
    total = 0
    for i in belts:
        if not belts[i]:
            continue
        if belts[i][0][1] <= w:
            box_id, box_weigth = belts[i].popleft()
            del id_belts[box_id]
            del id_weight[box_id]
            total += box_weigth
        else:
            # 벨트 맨 뒤로 상자 보내기
            belts[i].rotate(-1)
            # belts[i].popleft()
            # belts[i].append(first_box)
    print(total)
    return


# 공장 설립
def cmd_100(n, m, line):
    global belts, id_belts, id_weight, belts_status
    belts = {i: deque() for i in range(1, m + 1)}
    box_id = [int(next(line)) for _ in range(n)]
    box_weight = [int(next(line)) for _ in range(n)]

    j = 0
    for i in range(1, m + 1):
        for _ in range(n // m):
            belts[i].append((box_id[j], box_weight[j]))
            id_belts[box_id[j]] = i
            id_weight[box_id[j]] = (box_id[j], box_weight[j])
            j += 1
    return


id_belts = dict()
id_weight = dict()
belts = dict()
belts_status = []
broken_belts = set()

q = int(input())
for _ in range(q):
    line = iter(input().split())
    cmd = int(next(line))
    if cmd == 100:
        # 공장 설립
        n, m = (int(next(line)), int(next(line)))
        cmd_100(n, m, line)
    elif cmd == 200:
        # 물건 하차
        w = int(next(line))
        cmd_200(w)

    elif cmd == 300:
        # 물건 제거
        id = int(next(line))
        cmd_300(id)

    elif cmd == 400:
        # 물건 확인
        id = int(next(line))
        cmd_400(id)

    elif cmd == 500:
        # 벨트 고장
        id = int(next(line))
        cmd_500(id)

