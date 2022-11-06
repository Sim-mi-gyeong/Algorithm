import sys
from collections import deque

input = sys.stdin.readline


class Box:
    def __init__(self, box_id):
        self.box_id = box_id
        self.prev = None
        self.next = None


class Belt:
    def __init__(self, belt_num):
        self.belt_num = belt_num
        self.front = None
        self.end = None
        self.cnt = 0

    # 상자 번호 오름차순으로 벨트에 상자 쌓기 - 벨트 뒤로 쌓기
    def push_end_box(self, box):
        if not self.front:
            self.front = box

        if self.end:
            self.end.next = box
            box.prev = self.end

        self.end = box
        self.cnt += 1

    # 벨트 앞으로 쌓기
    def push_front_box(self, box):

        if not self.end:
            self.end = box

        if self.front:
            self.front.prev = box
            box.next = self.front

        self.front = box
        self.cnt += 1

    # 벨트 앞에서 빼내기
    def drop_front_box(self):

        pop_box = self.front
        self.front = pop_box.next

        pop_box.next = None

        if self.front:
            self.front.prev = None
        else:
            self.end = None

        self.cnt -= 1

        return pop_box


class Factory:
    # 공장 설립
    def __init__(self, n, m, line):
        self.belts = [Belt(belt_num) for belt_num in range(1, n + 1)]
        self.boxes = dict()

        for i in range(m):
            box_id = i + 1
            belt_num = line[i]
            box = Box(box_id)
            self.belts[belt_num - 1].push_end_box(box)
            self.boxes[box_id] = box

    # 물건 모두 옮기기
    def cmd_200(self, m_src, m_dst):

        if self.belts[m_src - 1].cnt == 0 and self.belts[m_dst - 1].cnt == 0:
            return 0
        elif self.belts[m_src - 1].cnt == 0:
            return self.belts[m_dst - 1].cnt
        # 벨트 연결
        elif self.belts[m_dst - 1].cnt == 0:
            self.belts[m_dst - 1] = self.belts[m_src - 1]

            self.belts[m_src - 1] = Belt(m_src)

            return self.belts[m_dst - 1].cnt
        # 벨트 연결
        else:
            self.belts[m_src - 1].end.next = self.belts[m_dst - 1].front
            self.belts[m_dst - 1].front.prev = self.belts[m_src - 1].end
            self.belts[m_dst - 1].front = self.belts[m_src - 1].front

            self.belts[m_src - 1].front = None
            self.belts[m_src - 1].end = None

            self.belts[m_dst - 1].cnt += self.belts[m_src - 1].cnt
            self.belts[m_src - 1].cnt = 0

            return self.belts[m_dst - 1].cnt

    # 앞 물건만 교체하기
    def cmd_300(self, m_src, m_dst):
        src_front_box, dst_front_box = None, None

        if self.belts[m_src - 1].cnt == 0 and self.belts[m_dst - 1].cnt == 0:
            return 0

        if self.belts[m_src - 1].cnt > 0:
            src_front_box = self.belts[m_src - 1].drop_front_box()

        if self.belts[m_dst - 1].cnt > 0:
            dst_front_box = self.belts[m_dst - 1].drop_front_box()

        if src_front_box != None:
            self.belts[m_dst - 1].push_front_box(src_front_box)

        if dst_front_box != None:
            self.belts[m_src - 1].push_front_box(dst_front_box)

        return self.belts[m_dst - 1].cnt

    # 물건 나누기
    def cmd_400(self, m_src, m_dst):
        if self.belts[m_src - 1].cnt == 1:
            return self.belts[m_dst - 1].cnt

        tmpN = self.belts[m_src - 1].cnt
        q = deque()
        for _ in range(tmpN // 2):
            pop_box = self.belts[m_src - 1].drop_front_box()
            q.append(pop_box)
        while q:
            pop_box = q.pop()
            self.belts[m_dst - 1].push_front_box(pop_box)

        return self.belts[m_dst - 1].cnt

    # 선물 정보 얻기
    def cmd_500(self, p_num):
        a, b = -1, -1
        return_num = a + 2 * b

        if p_num not in self.boxes:
            return return_num

        p_num_box = self.boxes[p_num]

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
        c = self.belts[b_num - 1].cnt
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
