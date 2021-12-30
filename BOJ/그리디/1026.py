# 보물

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()   # a를 오름차순 정렬 -> b의 가장 큰 원소는 a의 가장 작은 원소와 곱해져야함 
b.sort(reverse=True)
sum = 0
for i in range(n):
    sum += a[i] * b[i]
print(sum)

# 확인하기
# b_tmp = sorted(b, reverse=True)
# b_idx = []
# for i in b:
#     b_idx.append(b_tmp.index(i))
# sum = 0
# for i in range(n):
#     sum += a[b_idx[i]] * b[i]
# print(sum)
