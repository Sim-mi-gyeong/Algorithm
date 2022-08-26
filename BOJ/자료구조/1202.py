# 보석도둑
# 가방에는 최대 한 개의 보석만 넣을 수 있다
import heapq

n, k = map(int, input().split())
heapJ, heapBag = [], []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(heapJ, (-v, m))

for _ in range(k):
    b = int(input())
    heapq.heappush(heapBag, -b)
ans = 0
while heapBag:
    # 물건에 대해
    if len(heapJ):
        popVal = heapq.heappop(heapJ)
        print("popVal : ", popVal)
        price, weight = -popVal[0], popVal[1]
        print("price, weight : ", price, weight)
    else:
        break
    # 가방 가능 무게에 대해
    if len(heapBag):
        popBagVal = -heapBag[0]
        print("popBagVal : ", popBagVal)
    else:
        break

    if weight <= popBagVal:
        ans += price
        heapq.heappop(heapBag)
    else:
        continue

print(ans)


"""
이 문제의 조건으로 만들 수 있는 가장 큰 값은 300,000,000,000(=300,000*1,000,000) 

가방이랑 보석이 모두 최대 개수라고 가정해보세요
보석을 담을 수 있는 가방을 찾을 때 시간이 너무 오래 걸립니다.
해당 과정을 더 짧은 시간 안에 해결할 수 있도록 바꿔보세요
"""

"""
4 2
4 100
5 110
6 90
7 80
5
7

answer : 210
"""
