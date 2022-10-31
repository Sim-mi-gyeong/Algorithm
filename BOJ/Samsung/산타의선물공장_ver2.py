from collections import deque
import sys

input = sys.stdin.readline

### 전체 벨트에 대해 반복문을 돌던 부분을 수정해야 시간 초과 해결 가능
### 즉, id 처리만으로 가능한 것은 벨트 딕셔너리 반복문 돌지 않도록

# 벨트 고장

# 1. 고장난 벨트 번호에 고장 발생
# 2. b_num 오른쪽 벨트부터 순서대로 보며 -> 아직 고장이 나지 않은 최초의 벨트 위로
# -> b_num 벨트에 놓여있던 상자들을 아래에서부터 순서대로 하나씩 옮겨준다.
# 3. 만약, m 번까지 고장나지 않은 벨트가 없는 경우 -> 1번부터 다시 확인
# 4. 고장 처리 후 b_num 출력 / 이미 망가져 있는 경우 -1
# 각 벨트의 상태를 저장하는 부분이 필요!?
def cmd_500(b_num):
    if not belts_status[b_num]:
        print(-1)
        return

    # 고장 처리
    belts_status[b_num] = 0
    # b_num 이후부터 한 번씩 보면서 -> b_num - 1 까지
    for b in range(b_num + 1, m + 1):
        if belts_status[b]:
            # print("고장난 벨트의 상자를 옮길 벨트 번호 : ", b)
            # print("고장난 벨트의 상자를 옮기기 전 옮길 벨트 상태 : ", belts[b])
            # 벨트 아래 상자부터 옮기고
            while belts[b_num]:
                move_box = belts[b_num].popleft()
                move_box_id = move_box[0]
                belts[b].append(move_box)
                # 각 상자들이 속한 벨트 번호 바꿔주기 -> b로
                id_belts[move_box_id] = b

            # print("고장난 벨트의 상자를 옮긴 후 옮길 벨트 상태 : ", belts[b])
            print(b_num)
            return
    # 1번부터 다시 봐야 하는 경우
    for b in range(1, b_num):
        # print("고장난 벨트의 상자를 옮길 벨트 번호 : ", b)
        # print("고장난 벨트의 상자를 옮기기 전 옮길 벨트 상태 : ", belts[b])
        if belts_status[b]:
            # 벨트 아래 상자부터 옮기고
            while belts[b_num]:
                move_box = belts[b_num].popleft()
                move_box_id = move_box[0]
                belts[b].append(move_box)
                # 각 상자들이 속한 벨트 번호 바꿔주기 -> b로
                id_belts[move_box_id] = b

            # print("고장난 벨트의 상자를 옮긴 후 옮길 벨트 상태 : ", belts[b])
            print(b_num)
            return


def cmd_500_2(b_num):
    global belts, id_belts, belts_status, broken_belts
    if b_num in broken_belts:
        print(-1)
        return

    ### 고장난 벨트에 존재하는 상자들을 옮길 다른 벨트를 찾는 시간 줄이기
    ### 만약, 애초에 고장날 벨트가 마지막 벨트라면, 1번 벨트부터 찾도록
    if b_num == len(belts):
        next_belt = 1
    else:
        next_belt = b_num + 1
    while next_belt in broken_belts:
        next_belt = b_num + 1 if b_num != len(belts) else 1
    broken_belts.add(b_num)
    # 기존에 고장난 벨트에 있던 상자들을 새로운 벨트로 옮겨주기 -> 옮겨갈 벨트의 뒤에서 부터 하나씩 넣어주기
    belts[next_belt].extend(belts[b_num])
    del belts[b_num]
    # 옮겨간 상자들이 속한 벨트 번호 바꿔주기
    for box_id, box_belt in id_belts.items():
        if box_belt == b_num:
            id_belts[box_id] = next_belt

    print(b_num)
    return


# def broken(b_num):
#     global belts, id_belt, broked
#     if b_num not in belts:
#         b_num = -1
#         print(b_num)
#         return
#     next_belt = b_num + 1 if b_num != len(belts) else 1
#     while next_belt in broked:
#         next_belt = b_num + 1 if b_num != len(belts) else 1
#     broked.add(b_num)
#     belts[next_belt].extend(belts[b_num])
#     del belts[b_num]
# for r_id, b in id_belt.items():
#     if b == b_num:
#         id_belt[r_id] = next_belt
#     print(b_num)
#     return

# 물건 확인
# 1. 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면
# 1-1. 해당 벨트 번호 출력
# 1-2. "그 상자 위에 놓여있는 모든 상자"를 전부 앞으로 가져오기
# - 자신 포함 !!!!!!
# - 그 상자 뒤부터 빼내서 (pop) -> 앞으로 넣어주기 (appendleft)
# 2. 없다면 -> -1 출력

### 현재, 각 벨트 정보를 돌면서 (m) * 벨트 내의 상자들을 하나씩 (n) 확인
def cmd_400(id):
    for i in range(1, m + 1):
        # 벨트에 상자가 아무것도 없다면 넘어가기
        if not belts[i]:
            continue
        target_idx = -1
        for j in range(len(belts[i])):  # 각 벨트에 존재하는 상자들
            box = belts[i][j]
            box_id, box_weight = box[0], box[1]
            if id == box_id:
                # target_idx = j + 1
                target_idx = j
                print(i)  # 벨트 번호 출력
                break

        if target_idx == -1:  # 이 벨트에는 없는 경우
            continue
        else:  # 해당 벨트에 있는 경우
            # 그 상자 위에 놓여있는 모든 상자를 전부 앞으로 가져오기
            for next_j in range(target_idx, len(belts[i])):
                move_box = belts[i][next_j]
                move_box = belts[i].pop()
                belts[i].appendleft(move_box)
            return

    print(-1)


def cmd_400_2(id):
    global belts, id_belts
    target_b_num = -1
    if id in id_belts:
        target_b_num = id_belts[id]
        # print("찾는 상자가 있는 벨트 : ", target_b_num)
        while belts[target_b_num][0][0] != id:
            # belts[target_b_num].appendleft(belts[target_b_num].pop())
            belts[target_b_num].rotate(-1)

    print(target_b_num)
    return


# 물건 제거
# 1. 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면 -> 벨트에서 제거 & 뒤의 상자 내려오도록 & id 출력
# 2. 그렇지 않다면, -1 출력

### 현재, 각 벨트 정보를 돌면서 (m) * 벨트 내의 상자들을 하나씩 (n) 확인
### 최대 1 0 * 10,000 * 10,000 * ... -> 10,000
### -> O(1) 만에 해결 가능 := 어떤 id 상자가 어떤 벨트에 있는지 저장한 id_belts 사용
def cmd_300(id):
    # 각 벨트에 대해 -> 각 상자를 보면서
    for i in range(1, m + 1):
        # 벨트에 상자가 아무것도 없다면 넘어가기
        if not belts[i]:
            continue
        for j in range(len(belts[i])):
            box = belts[i][j]
            box_id, box_weight = box[0], box[1]
            if id == box_id:
                belts[i].remove(box)
                print(box_id)
                return

    print(-1)


def cmd_300_2(id):
    global belts, id_belts, id_weight
    return_num = -1
    if id in id_belts:
        return_num = id
        # id 가 있는 벨트 번호
        b_num = id_belts[id]
        remove_box = id_weight[id]
        belts[b_num].remove(remove_box)  # deque 에서 remove 는 평균 덱의 원소 개수 -> (O(N))
        del id_belts[id]  # 딕셔너리 제거 O(1)
        del id_weight[id]  # 딕셔너리 제거 O(1)

    print(return_num)


# 물건 하차
# w_max : 산타가 원하는 상자 최대 무게
# 1. 1 ~ m 번 벨트의 맨 앞 상자 중 w_max 이하면 하차 -> 상자 한 칸씩 앞으로 내려오기
# 2. 그렇지 않으면 벨트 맨 뒤로 상자 보내기
def cmd_200(w):  # O(M)
    total = 0
    for i in range(1, m + 1):  # 각 벨트에 대해
        # 벨트의 맨 앞 상자를 체크
        # 벨트가 비어있는 경우! pass
        if not belts[i]:
            continue
        first_box = belts[i][0]  # 상자
        first_box_id, first_box_weight = first_box[0], first_box[1]
        if first_box_weight <= w:
            # 하차 - 이때 상자의 무게 저장
            belts[i].popleft()
            del id_belts[first_box_id]
            del id_weight[first_box_id]
            # print("하차 : ", belts[i].popleft())
            total += first_box_weight
        else:
            # 벨트 맨 뒤로 상자 보내기
            belts[i].popleft()
            belts[i].append(first_box)
    print(total)


def cmd_200_2(w):  # O(M)
    global belts, id_belts
    total = 0
    for i in belts:  # 각 벨트에 대해(i : key)
        # 벨트의 맨 앞 상자를 체크
        # 벨트가 비어있는 경우! pass
        if not belts[i]:
            continue
        first_box = belts[i][0]  # 상자
        first_box_id, first_box_weight = first_box[0], first_box[1]
        if first_box_weight <= w:
            # 하차 - 이때 상자의 무게 저장
            belts[i].popleft()
            del id_belts[first_box_id]
            del id_weight[first_box_id]
            # print("하차 : ", belts[i].popleft())
            total += first_box_weight
        else:
            # 벨트 맨 뒤로 상자 보내기
            belts[i].popleft()
            belts[i].append(first_box)
    print(total)
    return


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


# 공장 설립
# 각 벨트에 어떤 상자(id, 무게)가 놓여있는지 정보 피룡
# 어떤 id 를 가진 상자가 어느 벨트에 있는지 정보 필요
# 어떤 id 를 가진 상자가 무게가 무엇인지 정보 필요
def cmd_100(n, m, line):
    global belts, id_belts, id_weight, belts_status
    belts = {i: deque() for i in range(1, m + 1)}  # 각 벨트마다 큐 초기화
    belts_status = [1] * (m + 1)  # 초기 벨트 상태는 전부 정상
    box_id = [int(next(line)) for _ in range(n)]  # 상자 id 정보 입력받기
    box_weight = [int(next(line)) for _ in range(n)]  # 상자 무게 정보 입력받기

    j = 0
    for i in range(1, m + 1):
        for _ in range(n // m):
            belts[i].append((box_id[j], box_weight[j]))
            # 어떤 id 상자가, 어떤 벨트에 있는지 정보 {상자 id : 벨트 id}
            id_belts[box_id[j]] = i
            # 어떤 id 상자의 무게 정보 저장 {상자 id : (상자 id, 상자 무게)}
            id_weight[box_id[j]] = (box_id[j], box_weight[j])
            j += 1


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
        # m 개의 벨트, n 개의 선물 -> 순서대로 n/m 개씩 잘라 1번 벨트부터 ~ m번 벨트까지 올리기
        # id 먼저 n 개, 다음 w n개
        n, m = (int(next(line)), int(next(line)))
        cmd_100(n, m, line)
    elif cmd == 200:
        # 물건 하차
        # 하차된 상자 무게 총 합 출력
        w = int(next(line))
        # cmd_200(w)
        cmd_200_2(w)

    elif cmd == 300:
        # 물건 제거
        # 상자가 있는 경우 제거 후 r_id 값, 없다면 -1 출력
        id = int(next(line))
        # cmd_300(id)
        cmd_300_2(id)

    elif cmd == 400:
        # 물건 확인
        # 상자가 있는 경우 f_id (벨트 번호) 값, 없다면 -1 출력
        id = int(next(line))
        # cmd_400(id)
        cmd_400_2(id)

    elif cmd == 500:
        # 벨트 고장
        # 이미 망가져 있었다면 -1, 그렇지 않으면 고장 처리 후 b_num
        id = int(next(line))
        # cmd_500(id)
        cmd_500_2(id)


"""
13
100 12 3 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17
200 25
300 22
300 999
400 14
400 18
500 3
400 17
200 15
300 12
500 1
500 3
200 40

answer
35
22
-1
-1
3
3
1
11  <<
12
1
-1
15



오답
35
22
-1
-1
3
3
1
14  <<
12
1
-1
15



"""


"""
answer 
1  번 벨트 상태 :  deque([(17, 11), (21, 14), (12, 30), (20, 20), (15, 20), (10, 30), (18, 17)])
2  번 벨트 상태 :  deque([(19, 18), (25, 15)])

내 출력
1  번 벨트 상태 :  deque([(21, 14), (21, 14), (12, 30), (20, 20), (15, 20), (10, 30), (17, 11)])
하차된 상자 무게 합 :  14
2  번 벨트 상태 :  deque([(19, 18), (25, 15)])
"""

