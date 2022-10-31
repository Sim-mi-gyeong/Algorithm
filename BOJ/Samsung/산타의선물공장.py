import sys

input = sys.stdin.readline


class BOX:
    def __init__(self, box_id, box_weight, belt_num):
        self.box_id = box_id
        self.box_weight = box_weight
        self.belt_num = belt_num
        self.prev_box = None
        self.next_box = None

    def set_prev(self, prev_box):
        self.prev_box = prev_box

    def set_next(self, next_box):
        self.next_box = next_box

    def remove_prev(self):
        if self.prev_box == None:
            return
        self.prev_box = None

    # def remove_next(self):
    #     if self.next_box == None:
    #         return

    #     self.next_box.prev_box = None
    #     self.next_box = None

    def remove_box(self):

        if self.prev_box:
            self.prev_box.next_box = self.next_box
        if self.next_box:
            self.next_box.prev_box = self.prev_box

        self.prev_box = None
        self.next_box = None


class BELT:
    def __init__(self, belt_num):
        self.belt_num = belt_num
        self.front = None
        self.end = None
        self.box_dict = dict()
        self.broken = False

    # 벨트의 뒤로 상자 싣기
    def push_box(self, box):
        self.box_dict[box.box_id] = box

        if not self.front:
            self.front = box

        if self.end:
            self.end.set_next(box)
            box.set_prev(self.end)

        self.end = box

    # 벨트의 가장 첫 번째 상자 하차
    def drop_box(self):

        pop_box = self.front
        self.front = pop_box.next_box

        pop_box.next_box = None

        if self.front:
            self.front.remove_prev()
        else:
            self.end = None

        del self.box_dict[pop_box.box_id]

        return pop_box


class FACTORY:
    # 공장 설립
    def __init__(self, line):
        global n, m
        n, m, *boxes = line
        count = n // m
        self.belts = [BELT(num) for num in range(1, m + 1)]

        for idx, belt in enumerate(self.belts):
            for i in range(idx * count, (idx + 1) * count):
                belt.push_box(BOX(boxes[i], boxes[i + n], idx + 1))

    # 물건 하차
    def cmd_200(self, w_max):
        total = 0
        for belt in self.belts:
            if not belt.front:
                continue

            if belt.broken:
                continue

            pop_box = belt.drop_box()
            if pop_box.box_weight <= w_max:
                total += pop_box.box_weight
            else:
                belt.push_box(pop_box)

        return total

    # 물건 제거
    def cmd_300(self, box_id):
        return_num = -1

        for belt in self.belts:
            if box_id not in belt.box_dict:
                continue

            removed_box = belt.box_dict[box_id]

            if belt.front == removed_box:
                belt.front = removed_box.next_box
            if belt.end == removed_box:
                belt.end = removed_box.prev_box

            removed_box.remove_box()
            return_num = removed_box.box_id
            del belt.box_dict[removed_box.box_id]
            break

        return return_num

    # 물건 확인
    def cmd_400(self, box_id):
        return_num = -1

        for belt_id, belt in enumerate(self.belts):
            if box_id in belt.box_dict:
                check_box = belt.box_dict[box_id]

                if belt.front == None and belt.end == None:
                    pass

                elif belt.front == check_box:
                    pass

                elif belt.end == check_box:
                    belt.front.set_prev(belt.end)
                    belt.end.set_next(belt.front)
                    belt.front = check_box
                    belt.end = check_box.prev_box
                    check_box.remove_prev()

                else:
                    belt.front.set_prev(belt.end)
                    belt.end.set_next(belt.front)
                    belt.front = check_box
                    belt.end = check_box.prev_box
                    check_box.remove_prev()

                if belt.front != check_box:
                    belt.front.set_prev(belt.end)
                    belt.end.set_next(belt.front)
                    belt.front = check_box
                    belt.end = check_box.prev_box
                    check_box.remove_prev()

                return_num = belt.belt_num
                # return_num = belt_id + 1
                break

        return return_num

    # 벨트 고장
    def cmd_500(self, b_num):
        return_num = -1

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

        target_belt.box_dict.update(broken_belt.box_dict)

        target_belt.end.next_box = broken_belt.front
        broken_belt.front.prev_box = target_belt.end

        for key, val in broken_belt.box_dict.items():
            val.belt_num = target_b_num

        target_belt.end = broken_belt.end

        broken_belt.box_dict = dict()

        broken_belt.front = broken_belt.end = None

        return return_num


q = int(input().strip())
cmd, *line = map(int, input().split())

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
