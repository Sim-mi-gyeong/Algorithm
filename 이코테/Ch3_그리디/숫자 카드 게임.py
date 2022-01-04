n, m = map(int, input().split())
card = [sorted(list(map(int, input().split()))) for _ in range(n)]
min = []
for i in card:
    min.append(i[0])
print(max(min))

# Sample Code 1 - min() 함수 사용
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     data = list(map(int, input().split))
#     min_val = min(data)
#     result = max(result, min_val)
# print(result)

# Sample Code 2 - 이중 반복문 구조
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_val = 10001
#     for j in data:
#         min_val = min(min_val, j)
#     result = max(result, min_val)
# print(result)