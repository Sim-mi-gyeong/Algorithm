graph = [[i * 5 + j for j in range(5)] for i in range(5)]
print(graph)

graph = [[0] * 5 for _ in range(5)]
for i in range(5):  # 0 ~ 4
    for j in range(5):  # 0 ~ 4
        graph[i][j] = i * 5 + 1 + j

print(graph)

graph = [[0] * 5 for _ in range(5)]
num = 1
for i in range(5):  # 0 ~ 4
    for j in range(5):  # 0 ~ 4
        graph[i][j] = num
        num += 1

print(graph)

print()
print("그래프 행 단위 추출")
for i in range(len(graph)):
    print(graph[i])


print()
print("그래프 열 단위 추출")
print("그래프 2열 추출")  # 3 8 13 18 23
print([i[2] for i in graph])
# print(graph[:][1])

print("graph[:] : ", graph[:])

print()
print("딕셔너리 초기화 테스트")
# group_edges.get(arr[nr][nc], 0)
dic = dict()
for i in range(3):
    for j in range(3):
        dic[i] = dic.get(i, 1) + 1  # dic 의 key 값이 i 일 때 value 값을 1로 초기화
        # dic[i] += 1

print(dic)
