import sys
from collections import Counter

sys.setrecursionlimit(100005)

input = sys.stdin.readline
n = int(input())

move = list(map(lambda x: int(x) - 1, input().split()))
nums = list(map(int, input().split()))
# Cycle Detectins 과정에서 같은 사이클을 여러 번 찾지 않기 위해 Cycle Detectins 이 된 정점에 방문 처리
visited = [False for _ in range(n)]

# 자기가 가리키는 방향을 따라 계속 이동
# 현재 내가 idx 위치에 있으면 -> 다음으로 move[idx] 로 갈 것
def traverse(idx, find_nums):
    find_nums.append(nums[idx])  # nums[idx] : 현재 위치에 있는 카드를 찾고 -> find_nums 에 기록
    visited[idx] = True  # 해당 위치 방문 처리
    if not visited[move[idx]]:
        traverse(move[idx], find_nums)
        if not visited[move[idx]]:  # 현재 내가 다음으로 갈 위치를 아직 방문하지 않았다면,
            traverse(move[idx], find_nums)  # 재귀 호출


ans = 0
# 모든 정점을 한 번씩 보면서,
for i in range(n):
    if visited[i]:  # 해당 점정이 속한 사이클이 아직 Detection 이 되지 않았다면,
        continue
    find_nums = []
    traverse(i, find_nums)  # 해당 점정으로부터 시작해서 -> 전부 사이클을 찾고
    counter = Counter(find_nums)  # 최빈값을 찾아
    freq = max(counter.values())
    ans += len(find_nums) - freq  # 사이클의 길이 - 최빈값 = 바꾸어야 할 사람의 횟수

print(ans)


"""
6
2 1 4 5 3 6
1 1 2 2 1 1

ans : 1

4
2 3 4 1
1 2 3 4

ans : 3
"""
