import sys

input = sys.stdin.readline


class Box:
    def __init__(self, box_id, belt_num):
        self.box_id = box_id
        self.prev = None
        self.next = None


class Belt:
    def __init__(self, belt_num):
        self.belt_num = belt_num
        self.front = None
        self.end = None
        self.box_dict = dict()

    # 상자 번호 오름차순으로 벨트에 상자 쌓기 - 벨트 뒤로 쌓기
    def push_end_box(self, box):
        self.box_dict[box.box_id] = box

        if not self.front:
            self.front = box

        if self.end:
            self.end.next = box
            box.prev = self.end
        self.end = box

    # 벨트 앞으로 쌓기
    def push_front_box(self, box):
        self.box_dict[box.box_id] = box
        if not self.end:
            self.end = box

        if self.front:
            self.front.prev = box
            box.next = self.front
        self.front = box

    # 벨트 앞에서 빼내기
    def drop_front_box(self):

        pop_box = self.front
        self.front = pop_box.next

        pop_box.next = None

        if self.front:
            self.front.prev = None
        else:
            self.end = None

        del self.box_dict[pop_box.box_id]

        return pop_box


class Factory:
    # 공장 설립
    def __init__(self, n, m, line):
        self.belts = [Belt(belt_num) for belt_num in range(1, n + 1)]
        for i in range(m):
            box_id = i + 1
            belt_num = line[i]
            self.belts[belt_num - 1].push_end_box(Box(box_id, belt_num))

    # 물건 모두 옮기기
    def cmd_200(self, m_src, m_dst):
        if not self.belts[m_src - 1].front:
            return len(self.belts[m_dst - 1].box_dict)

        src_belt = self.belts[m_src - 1]
        dst_belt = self.belts[m_dst - 1]

        # 벨트 연결
        if src_belt.end == None and dst_belt.front:
            dst_belt.front.prev = src_belt.end
            dst_belt.front = src_belt.front
        elif dst_belt.front == None and src_belt.end:
            src_belt.end.next = dst_belt.front
            dst_belt.front = src_belt.front
        elif src_belt.end == None and dst_belt.front == None:
            pass
        else:
            src_belt.end.next = dst_belt.front
            dst_belt.front.prev = src_belt.end
            dst_belt.front = src_belt.front

        dst_belt.box_dict.update(src_belt.box_dict)
        src_belt.box_dict = dict()

        src_belt.front = None
        src_belt.end = None

        dst_belt_box_num = len(dst_belt.box_dict)
        return dst_belt_box_num

    # 앞 물건만 교체하기
    def cmd_300(self, m_src, m_dst):
        if self.belts[m_src - 1].front == None and self.belts[m_dst - 1].front == None:
            return len(self.belts[m_dst - 1].box_dict)
        elif self.belts[m_src - 1].front == None and self.belts[m_dst - 1].front:
            dst_front_box = self.belts[m_dst - 1].drop_front_box()
            self.belts[m_src - 1].push_front_box(dst_front_box)

            return len(self.belts[m_dst - 1].box_dict)

        elif self.belts[m_src - 1].front and self.belts[m_dst - 1].front == None:
            src_front_box = self.belts[m_src - 1].drop_front_box()
            self.belts[m_dst - 1].push_front_box(src_front_box)

            return len(self.belts[m_dst - 1].box_dict)

        elif self.belts[m_src - 1].front and self.belts[m_dst - 1].front:
            src_front_box = self.belts[m_src - 1].drop_front_box()
            dst_front_box = self.belts[m_dst - 1].drop_front_box()

            self.belts[m_dst - 1].push_front_box(src_front_box)
            self.belts[m_src - 1].push_front_box(dst_front_box)

            return len(self.belts[m_dst - 1].box_dict)

    # 물건 나누기
    def cmd_400(self, m_src, m_dst):
        if len(self.belts[m_src - 1].box_dict) == 1:
            return len(self.belts[m_dst - 1].box_dict)

        tmpN = len(self.belts[m_src - 1].box_dict)
        for i in range(tmpN // 2):
            pop_box = self.belts[m_src - 1].drop_front_box()
            self.belts[m_dst - 1].push_front_box(pop_box)

        return len(self.belts[m_dst - 1].box_dict)

    # 선물 정보 얻기
    def cmd_500(self, p_num):
        return_num = -1 + 2 * (-1)
        for b_num in range(1, len(self.belts) + 1):
            if p_num not in self.belts[b_num - 1].box_dict:
                continue
            p_num_box = self.belts[b_num - 1].box_dict[p_num]
            a, b = -1, -1
            prev_p_num_box = p_num_box.prev
            if prev_p_num_box != None:
                a = prev_p_num_box.box_id
            next_p_num_box = p_num_box.next
            if next_p_num_box != None:
                b = next_p_num_box.box_id
            return_num = a + 2 * b

        return return_num

    # 벨트 정보 얻기
    def cmd_600(self, b_num):
        return_num = -1 + 2 * (-1) + 0
        a, b, c = -1, -1, 0
        front_box = self.belts[b_num - 1].front
        if front_box != None:
            a = front_box.box_id
        end_box = self.belts[b_num - 1].end
        if end_box != None:
            b = end_box.box_id
        c = len(self.belts[b_num - 1].box_dict)
        return_num = a + 2 * b + 3 * c

        return return_num


def init_input():
    q = int(input())
    cmd, n, m, *line = map(int, input().split())
    factory = Factory(n, m, line)

    for _ in range(q - 1):
        line = iter(input().split())
        cmd = int(next(line))
        if cmd == 200:
            m_src, m_dst = int(next(line)), int(next(line))
            print(factory.cmd_200(m_src, m_dst))
        elif cmd == 300:
            m_src, m_dst = int(next(line)), int(next(line))
            print(factory.cmd_300(m_src, m_dst))
        elif cmd == 400:
            m_src, m_dst = int(next(line)), int(next(line))
            print(factory.cmd_400(m_src, m_dst))
        elif cmd == 500:
            p_num = int(next(line))
            print(factory.cmd_500(p_num))
        elif cmd == 600:
            b_num = int(next(line))
            print(factory.cmd_600(b_num))


init_input()
