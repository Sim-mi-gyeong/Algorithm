# Union-Find
def find_parent(a, parent):
    if a != parent[a]:
        return find_parent(parent[a], parent)
    return parent[a]


def union(a, b):
    parentA = find_parent(a, parent)
    parentB = find_parent(b, parent)
    if parentA != parentB:
        parent[parentB] = parentA


def solution(n, wires):
    global parent
    answer = 1e9

    # wires 중에서 어디를 자를지 정하고 -> 각 전력망에 연결된 송전탑 개수 체크
    for wire in wires:
        tmp = wires[:]
        tmp.remove(wire)  # 한 개의 전선 끊기

        parent = [i for i in range(n + 1)]

        for a, b in tmp:
            if find_parent(a, parent) != find_parent(b, parent):
                union(a, b)  # 연결된 전선끼리 그래프 구성

        dic = dict()  # 루트 노드(루트 전력망) 이 가지고 있는 송전탑 개수 기록
        for p in parent[1:]:
            parentP = find_parent(p, parent)
            if parentP not in dic:
                dic[parentP] = 1
            else:
                dic[parentP] += 1

        values = list(dic.values())

        tmpVal = abs(values[0] - values[1])

        if tmpVal < answer:
            answer = tmpVal

    return answer
