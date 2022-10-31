from collections import deque
import sys

input = sys.stdin.readline


class BOX:
    def __init__(self, box_id, box_weight, belt_num):
        self.box_id = box_id
        self.box_weight = box_weight
        self.belt_num = belt_num
        self.prev_box = None
        self.next_box = None
        # self.box_belt = dict()  # 상자 id 가 어떤 belt 에 속해있는지 저장

    # 파라미터 안의 상자를 자신의 prev link 로 설정
    def set_prev(self, prev_box):
        self.prev_box = prev_box

    # 파라미터 안의 상자를 자신의 next link 로 설정
    def set_next(self, next_box):
        self.next_box = next_box

    # 벨트의 첫 번째 상자가 된 경우 / 벨트 앞에서 상자를 빼낸 경우 -> prev link 끊어주기
    def remove_prev(self):
        if self.prev_box == None:
            return

        # self.next_box.prev_box = None   # 벨트의 front 를 바꾼 후 이미 처리
        self.prev_box = None

    #  벨트의 마지막 상자가 된 경우 / 벨트 뒤에서 상자를 빼낸 경우 -> next link 끊어주기
    # def remove_next(self):
    #     if self.next_box == None:
    #         return

    #     self.next_box.prev_box = None
    #     self.next_box = None

    def remove_box(self):

        # 제거할 상자가 벨트의 front 혹은 end 일 경우 상자 제거 후 front / end 상태 처리가 완료된 상태
        # 상자 제거 후, 제거할 상자 prev, next 상자 간 link 처리
        if self.prev_box:
            self.prev_box.next_box = self.next_box
        if self.next_box:
            self.next_box.prev_box = self.prev_box

        # 상자 제거 -> 제거할 상자의 prev, next link 제거
        self.prev_box = None
        self.next_box = None


class BELT:
    def __init__(self, belt_num):
        self.belt_num = belt_num
        self.front = None  # 벨트의 가장 첫 번째 상자
        self.end = None  # 벨트의 가장 마지막 상자
        self.box_dict = dict()  # 벨트에 존재하는 각 상자들의 정보를 저장하는 딕셔너리 -> {상자 id : 상자 object}
        self.broken = False

    # 벨트의 뒤로 상자 싣기
    def push_box(self, box):  # box = BOX() 객체
        self.box_dict[box.box_id] = box

        if not self.front:  # 가장 첫 번째 상자가 존재하지 않는 경우 -> 현재 들어온 상자를 첫 번째 상자로
            self.front = box

        if self.end:  # 이미 마지막 상자가 존재한다면 -> 새로 들어온 상자와 link 처리
            self.end.set_next(box)  # 기존 벨트의 end 상자를 새로 들어온 상자로 설정
            box.set_prev(self.end)  # 기존 벨트의 end 상자를 새로 들어온 상자의 prev_box 로 설정

        # 들어오는 상자마다 마지막 상자 처리
        self.end = box

    # 벨트의 가장 첫 번째 상자 하차
    def drop_box(self, box):

        # 벨트의 front 를 하차할 상자 다음 상자로 바꾸기
        self.front = box.next_box

        # 하차할 상자의 next link 끊어주기
        box.next_box = None

        # 이때, 상자 하차로 벨트가 빈 상태가 될 수도 있으므로 null 체크
        # 상자 하차 이후에도 상자가 남아있다면 -> 앞 상자 하차로 front 가 된 상자의 prev 제거
        if self.front:
            self.front.remove_prev()
        # 상자 하차 이후 벨트가 빈 상태라면 (self.front = None) -> 벨트의 마지막 상자도 None
        else:
            self.end = None

        del self.box_dict[box.box_id]

        return box


class FACTORY:
    # 공장 설립
    def __init__(self, line):
        global n, m
        n, m, *boxes = line
        print("n: ", n, " m : ", m, " boxes : ", boxes)
        count = n // m
        self.belts = [BELT(num) for num in range(1, m + 1)]  # m 개 벨트 리스트 생성
        # self.box_belt = dict()
        # 각 벨트마다 순차적으로 상자 추가

        cnt = 0
        for idx, belt in enumerate(self.belts):
            for i in range(idx * count, (idx + 1) * count):
                cnt += 1
                belt.push_box(BOX(boxes[i], boxes[i + n], idx + 1))
                # self.box_belt[line[i]] = BOX(line[i], line[i + n], idx + 1)  # {상자 id : BOX object}
        print("push 완료 후 cnt : ", cnt)

    # 물건 하차 (O(M))
    def cmd_200(self, w_max):
        total = 0
        for belt in self.belts:
            # 벨트가 비어있는 경우 pass
            if not belt.front:
                continue
            # 고장난 벨트인 경우 pass
            if belt.broken:
                continue
            # 벨트의 첫 번째 상자가 존재하는 경우에 대해
            if belt.front.box_weight <= w_max:
                total += belt.front.box_weight

                # 하차
                belt.drop_box(belt.front)
            else:
                # 하차 후
                belt.drop_box(belt.front)
                # 다시 싣기
                belt.push_box(belt.front)

            print("total : ", total)

        return total

    # 물건 제거 (O(1) -> O(M))
    def cmd_300(self, box_id):
        return_num = -1

        for belt in self.belts:  # O(M)
            # 벨트에 상자가 없는 경우 pass
            print("belt.box_dic : ", belt.box_dict)
            # if box_id not in belt.box_dict:
            #     continue
            if box_id in belt.box_dict:
                removed_box = belt.box_dict[box_id]
                # 상자 제거 후 벨트의 front 와 end 상태 처리
                # 제거할 상자가 벨트의 가장 첫번째 상자라면
                if belt.front == removed_box:
                    # 제거하기 전 첫 번째 상자의 다음 상자를 -> 벨트의 첫 번째 상자로
                    belt.front = removed_box.next_box
                # 제거할 상자가 벨트의 가장 마지막 상자라면
                if belt.end == removed_box:
                    # 제거하기 전 마지막 상자의 이전 상자를 -> 벨트의 가장 마지막 상자로
                    belt.end = removed_box.prev_box

                removed_box.remove_box()
                return_num = removed_box.box_id
                del belt.box_dict[removed_box.box_id]
                break

        return return_num
        # removed_box = self.box_belt[box_id]

    # 물건 확인 (O(1) -> O(M))
    # 1. 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면
    # 1-1. 해당 벨트의 번호를 출력하고,
    # 1-2. 해당 상자 포함 위의 상자를 벨트 앞으로 순서대로 가져오기
    # 2. 없다면 -1을 출력
    def cmd_400(self, box_id):
        return_num = -1

        for belt_id, belt in enumerate(self.belts):
            print("belt_id : ", belt_id, " belt : ", belt)
            if box_id in belt.box_dict:
                check_box = belt.box_dict[box_id]
                # 벨트가 비어있는 경우
                # if belt.front == None and belt.end == None:
                #     pass
                # # 찾는 상자가 벨트 가장 앞에 위치한 경우
                # elif belt.front == check_box:
                #     pass
                # # 찾는 상자가 벨트 가장 뒤에 위치한 경우 -> 찾는 상자를 가장 앞으로
                # elif belt.end == check_box:
                #     # 옮겨야할 상자의 상태는 마지막으로 변경
                #     # -> 상자를 옮김으로써 발생하는 다른 상자들의 prev, next link 를 먼저 처리
                #     belt.front.set_prev(belt.end)
                #     belt.end.set_next(belt.front)
                #     belt.front = check_box
                #     belt.end = check_box.prev_box
                #     check_box.remove_prev()
                # # 찾는 상자가 벨트 중간에 위치한 경우
                # else:
                #     belt.front.set_prev(belt.end)  # belt 의 front link
                #     belt.end.set_next(belt.front)  # belt 의 end link
                #     belt.front = check_box  # belt 의 front
                #     belt.end = check_box.prev_box  # belt 의 end
                #     check_box.remove_prev()

                if belt.front != check_box:
                    belt.front.set_prev(belt.end)
                    belt.end.set_next(belt.front)
                    belt.front = check_box
                    belt.end = check_box.prev_box
                    check_box.remove_prev()

                # return_num = belt.belt_num
                return_num = belt_id + 1
                break

        return return_num

    # 벨트 고장 (O(N) 이지만, 최대 9번까지 가능하기 때문에 시간초과 X)
    def cmd_500(self, b_num):
        return_num = -1
        # 이미 벨트가 고장난 경우
        if self.belts[b_num - 1].broken:
            return return_num

        return_num = b_num
        broken_belt = self.belts[b_num - 1]
        broken_belt.broken = True

        target_b_num = b_num
        while self.belts[target_b_num - 1].broken:
            target_b_num += 1
            if target_b_num > m:
                target_b_num = 1

        target_belt = self.belts[target_b_num - 1]
        # 고장난 벨트에 있던 상자들을 옮겨갈 벨트의 상자 정보에 추가
        target_belt.box_dict.update(broken_belt.box_dict)

        # 1. target belt end 와 broken belt front 사이에 link 생성
        target_belt.end.next_box = broken_belt.front
        broken_belt.front.prev_box = target_belt.end

        # 2. broken_belt 의 상자들의 belt 번호를 -> target belt 의 belt_num 으로 변경   ### belt_num 을 직접적으로 쓰지 않아서 안 해도 됨
        for key, val in broken_belt.box_dict.items():
            # {box id : BOX}
            val.belt_num = target_b_num
        # 3. target belt 의 end 를 -> broken belt 의 end 로 변경
        target_belt.end = broken_belt.end

        # 고장난 벨트에 있던 상자 비우기
        broken_belt.box_dict = dict()

        # 4. broken belt 의 front 와 end 제거
        broken_belt.front = broken_belt.end = None

        return return_num


q = int(input())
cmd, *line = map(int, input().split())  # line -> list

factory = FACTORY(line)

for _ in range(q - 1):
    cmd, arg = map(int, input().split())

    if cmd == 200:
        print(factory.cmd_200(arg))
    elif cmd == 300:
        print(factory.cmd_300(arg))
    elif cmd == 400:
        print(factory.cmd_400(arg))
    elif cmd == 500:
        print(factory.cmd_500(arg))


"""
belt.box_dic :  {20: <__main__.BOX object at 0x7fbca825f490>, 
15: <__main__.BOX object at 0x7fbca825f4c0>, 
17: <__main__.BOX object at 0x7fbca825f8b0>, 
21: <__main__.BOX object at 0x7fbca825f910>, 
18: <__main__.BOX object at 0x7fbca825f970>}
belt.box_dic :  {25: <__main__.BOX object at 0x7fbca825f6d0>}
belt.box_dic :  {}

"""


"""
belt.box_dic :  {20: <__main__.Box object at 0x7fa2801d75e0>, 
15: <__main__.Box object at 0x7fa2801d75b0>,
10: <__main__.Box object at 0x7fa2801d7460>, 
17: <__main__.Box object at 0x7fa2801d79a0>, 
21: <__main__.Box object at 0x7fa2801d7760>, 
18: <__main__.Box object at 0x7fa2801d77c0>, 
12: <__main__.Box object at 0x7fa2801d74c0>}
"""

