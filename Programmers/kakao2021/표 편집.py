class Row:
    def __init__(self, row_id, prev, next):
        self.row_id = row_id
        self.removed = False  # 존재/삭제 여부
        self.prev = prev if prev >= 0 else None
        self.next = next if next < N else None


def solution(n, k, cmd):
    global deleteList, N
    N = n
    answer = ""
    deleteList = []
    row_list = [Row(row_id, row_id - 1, row_id + 1) for row_id in range(n)]
    now = k

    for tmp_cmd in cmd:
        tmp_cmd = tmp_cmd.split(" ")
        if tmp_cmd[0] == "U":
            for _ in range(int(tmp_cmd[1])):
                now = row_list[now].prev
        elif tmp_cmd[0] == "D":
            for _ in range(int(tmp_cmd[1])):
                now = row_list[now].next

        elif tmp_cmd[0] == "C":
            deleteList.append(now)
            row_list[now].removed = True

            if row_list[now].prev != None:
                row_list[row_list[now].prev].next = row_list[now].next

            if row_list[now].next != None:
                row_list[row_list[now].next].prev = row_list[now].prev

            if row_list[now].next == None:
                now = row_list[now].prev
            else:
                now = row_list[now].next

        elif tmp_cmd[0] == "Z":
            re_row = deleteList.pop()
            row_list[re_row].removed = False

            # 이전 노드와 다음 노드 링크 복구
            if row_list[re_row].prev != None:
                row_list[row_list[re_row].prev].next = re_row

            # 복구한 행의 prev, next 연결
            if row_list[re_row].next != None:
                row_list[row_list[re_row].next].prev = re_row

    for row in row_list:
        if row.removed:
            answer += "X"
        else:
            answer += "O"

    return answer
